"""
Teste automatizado para o site SauceDemo.
Este script implementa os casos de teste TC-001 e TC-002 para o site SauceDemo.

TC-001: Login bem-sucedido com usuário padrão (standard_user/secret_sauce).
TC-002: Login malsucedido com usuário inválido (invalid_user/wrong_password).
"""
import sys
import os
import time
from datetime import datetime

# Adicionar o diretório pai ao path para importar o módulo config_base
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from config_base import configurar_driver, registrar_inicio_teste, registrar_fim_teste, capturar_screenshot

# URLs e credenciais
URL = "https://www.saucedemo.com/"
USUARIO_VALIDO = "standard_user"
SENHA_VALIDA = "secret_sauce"
USUARIO_INVALIDO = "invalid_user"
SENHA_INVALIDA = "wrong_password"

def executar_tc001_login_sucesso():
    """
    TC-001: Teste de login bem-sucedido com usuário padrão.
    
    Returns:
        dict: Resultado do teste contendo status, mensagens e caminhos para screenshots.
    """
    # Inicializar resultado do teste
    resultado = {
        "id": "TC-001",
        "descricao": "Login bem-sucedido com usuário padrão",
        "status": "Falhou",
        "mensagens": [],
        "screenshots": [],
        "inicio": None,
        "fim": None,
        "duracao": None
    }
    
    # Registrar início do teste
    resultado["inicio"] = registrar_inicio_teste("TC-001: Login bem-sucedido")
    
    # Configurar driver
    driver = None
    try:
        driver = configurar_driver()
        resultado["mensagens"].append("Driver configurado com sucesso.")
        
        # Navegar para a página
        driver.get(URL)
        resultado["mensagens"].append(f"Navegou para {URL}")
        time.sleep(2)  # Aguardar carregamento da página
        
        # Capturar screenshot da página de login
        screenshot_login = capturar_screenshot(driver, "tc001_pagina_login")
        resultado["screenshots"].append(screenshot_login)
        
        # Preencher formulário de login
        driver.find_element("id", "user-name").send_keys(USUARIO_VALIDO)
        driver.find_element("id", "password").send_keys(SENHA_VALIDA)
        resultado["mensagens"].append(f"Preencheu credenciais: usuário={USUARIO_VALIDO}, senha={SENHA_VALIDA}")
        
        # Clicar no botão de login
        driver.find_element("id", "login-button").click()
        resultado["mensagens"].append("Clicou no botão de login")
        time.sleep(2)  # Aguardar redirecionamento
        
        # Verificar se o login foi bem-sucedido (verificando URL ou elemento da página de produtos)
        current_url = driver.current_url
        if "inventory.html" in current_url:
            resultado["status"] = "Passou"
            resultado["mensagens"].append("Login bem-sucedido! Redirecionado para a página de produtos.")
            
            # Capturar screenshot da página de produtos
            screenshot_produtos = capturar_screenshot(driver, "tc001_pagina_produtos")
            resultado["screenshots"].append(screenshot_produtos)
        else:
            resultado["status"] = "Falhou"
            resultado["mensagens"].append(f"Falha no login. URL atual: {current_url}")
            
            # Tentar capturar mensagem de erro, se houver
            try:
                erro_elemento = driver.find_element("css selector", ".error-message-container")
                erro_texto = erro_elemento.text
                resultado["mensagens"].append(f"Mensagem de erro: {erro_texto}")
            except Exception as e:
                resultado["mensagens"].append(f"Não foi possível capturar mensagem de erro: {str(e)}")
    
    except Exception as e:
        resultado["status"] = "Falhou"
        resultado["mensagens"].append(f"Erro durante a execução do teste: {str(e)}")
    
    finally:
        # Registrar fim do teste
        if driver:
            # Capturar screenshot final, independente do resultado
            screenshot_final = capturar_screenshot(driver, "tc001_final")
            resultado["screenshots"].append(screenshot_final)
            
            # Fechar o driver
            driver.quit()
            resultado["mensagens"].append("Driver fechado.")
        
        # Registrar tempo de execução
        resultado["fim"], resultado["duracao"] = registrar_fim_teste("TC-001: Login bem-sucedido", resultado["inicio"])
    
    return resultado

def executar_tc002_login_falha():
    """
    TC-002: Teste de login malsucedido com usuário inválido.
    
    Returns:
        dict: Resultado do teste contendo status, mensagens e caminhos para screenshots.
    """
    # Inicializar resultado do teste
    resultado = {
        "id": "TC-002",
        "descricao": "Login malsucedido com usuário inválido",
        "status": "Falhou",
        "mensagens": [],
        "screenshots": [],
        "inicio": None,
        "fim": None,
        "duracao": None
    }
    
    # Registrar início do teste
    resultado["inicio"] = registrar_inicio_teste("TC-002: Login malsucedido")
    
    # Configurar driver
    driver = None
    try:
        driver = configurar_driver()
        resultado["mensagens"].append("Driver configurado com sucesso.")
        
        # Navegar para a página
        driver.get(URL)
        resultado["mensagens"].append(f"Navegou para {URL}")
        time.sleep(2)  # Aguardar carregamento da página
        
        # Capturar screenshot da página de login
        screenshot_login = capturar_screenshot(driver, "tc002_pagina_login")
        resultado["screenshots"].append(screenshot_login)
        
        # Preencher formulário de login com credenciais inválidas
        driver.find_element("id", "user-name").send_keys(USUARIO_INVALIDO)
        driver.find_element("id", "password").send_keys(SENHA_INVALIDA)
        resultado["mensagens"].append(f"Preencheu credenciais inválidas: usuário={USUARIO_INVALIDO}, senha={SENHA_INVALIDA}")
        
        # Clicar no botão de login
        driver.find_element("id", "login-button").click()
        resultado["mensagens"].append("Clicou no botão de login")
        time.sleep(2)  # Aguardar resposta
        
        # Verificar se apareceu mensagem de erro
        try:
            erro_elemento = driver.find_element("css selector", ".error-message-container")
            erro_texto = erro_elemento.text
            resultado["mensagens"].append(f"Mensagem de erro exibida: {erro_texto}")
            
            # Capturar screenshot da mensagem de erro
            screenshot_erro = capturar_screenshot(driver, "tc002_mensagem_erro")
            resultado["screenshots"].append(screenshot_erro)
            
            # Verificar se ainda estamos na página de login (não redirecionou)
            if "inventory.html" not in driver.current_url:
                resultado["status"] = "Passou"
                resultado["mensagens"].append("Teste passou: Login falhou conforme esperado e exibiu mensagem de erro.")
            else:
                resultado["status"] = "Falhou"
                resultado["mensagens"].append("Teste falhou: Login com credenciais inválidas foi bem-sucedido, o que não era esperado.")
        
        except Exception as e:
            resultado["status"] = "Falhou"
            resultado["mensagens"].append(f"Não foi possível encontrar mensagem de erro: {str(e)}")
    
    except Exception as e:
        resultado["status"] = "Falhou"
        resultado["mensagens"].append(f"Erro durante a execução do teste: {str(e)}")
    
    finally:
        # Registrar fim do teste
        if driver:
            # Capturar screenshot final, independente do resultado
            screenshot_final = capturar_screenshot(driver, "tc002_final")
            resultado["screenshots"].append(screenshot_final)
            
            # Fechar o driver
            driver.quit()
            resultado["mensagens"].append("Driver fechado.")
        
        # Registrar tempo de execução
        resultado["fim"], resultado["duracao"] = registrar_fim_teste("TC-002: Login malsucedido", resultado["inicio"])
    
    return resultado

def salvar_resultado_para_relatorio(resultado, arquivo_saida):
    """
    Salva o resultado do teste em um arquivo para posterior geração de relatório.
    
    Args:
        resultado (dict): Resultado do teste.
        arquivo_saida (str): Caminho para o arquivo de saída.
    """
    with open(arquivo_saida, 'w', encoding='utf-8') as f:
        f.write(f"# Relatório de Teste: {resultado['id']} - {resultado['descricao']}\n\n")
        f.write(f"## Informações Gerais\n")
        f.write(f"- **ID do Teste**: {resultado['id']}\n")
        f.write(f"- **Descrição**: {resultado['descricao']}\n")
        f.write(f"- **Status**: {resultado['status']}\n")
        f.write(f"- **Data/Hora de Início**: {resultado['inicio']}\n")
        f.write(f"- **Data/Hora de Término**: {resultado['fim']}\n")
        f.write(f"- **Duração**: {resultado['duracao']:.2f} segundos\n\n")
        
        f.write(f"## Passos Executados\n")
        for i, mensagem in enumerate(resultado['mensagens'], 1):
            f.write(f"{i}. {mensagem}\n")
        
        f.write(f"\n## Screenshots\n")
        for screenshot in resultado['screenshots']:
            nome_arquivo = os.path.basename(screenshot)
            f.write(f"- {nome_arquivo}\n")

if __name__ == "__main__":
    # Criar diretório para resultados se não existir
    resultados_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "relatorios")
    if not os.path.exists(resultados_dir):
        os.makedirs(resultados_dir)
    
    # Executar TC-001: Login bem-sucedido
    resultado_tc001 = executar_tc001_login_sucesso()
    arquivo_resultado_tc001 = os.path.join(resultados_dir, "resultado_tc001.md")
    salvar_resultado_para_relatorio(resultado_tc001, arquivo_resultado_tc001)
    print(f"Resultado do TC-001 salvo em: {arquivo_resultado_tc001}")
    
    # Executar TC-002: Login malsucedido
    resultado_tc002 = executar_tc002_login_falha()
    arquivo_resultado_tc002 = os.path.join(resultados_dir, "resultado_tc002.md")
    salvar_resultado_para_relatorio(resultado_tc002, arquivo_resultado_tc002)
    print(f"Resultado do TC-002 salvo em: {arquivo_resultado_tc002}")
    
    # Imprimir resumo dos resultados
    print("\nResumo dos Resultados:")
    print(f"TC-001: {resultado_tc001['status']}")
    print(f"TC-002: {resultado_tc002['status']}")
