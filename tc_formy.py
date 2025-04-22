"""
Teste automatizado para o site Formy.
Este script implementa o caso de teste TC-005 para o site Formy.

TC-005: Preencher todos os campos do formulário e submeter.
"""
import sys
import os
import time
from datetime import datetime

# Adicionar o diretório pai ao path para importar o módulo config_base
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from config_base import configurar_driver, registrar_inicio_teste, registrar_fim_teste, capturar_screenshot

# Importar classes específicas para interação com elementos
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

# URL do site
URL = "https://formy-project.herokuapp.com/form"

def executar_tc005_formy_formulario():
    """
    TC-005: Teste de preenchimento de formulário no site Formy.
    
    Returns:
        dict: Resultado do teste contendo status, mensagens e caminhos para screenshots.
    """
    # Inicializar resultado do teste
    resultado = {
        "id": "TC-005",
        "descricao": "Preenchimento de formulário no Formy",
        "status": "Falhou",
        "mensagens": [],
        "screenshots": [],
        "inicio": None,
        "fim": None,
        "duracao": None,
        "dados_formulario": {}
    }
    
    # Registrar início do teste
    resultado["inicio"] = registrar_inicio_teste("TC-005: Formy - Preenchimento de Formulário")
    
    # Configurar driver
    driver = None
    try:
        driver = configurar_driver()
        resultado["mensagens"].append("Driver configurado com sucesso.")
        
        # Navegar para a página
        driver.get(URL)
        resultado["mensagens"].append(f"Navegou para {URL}")
        time.sleep(2)  # Aguardar carregamento inicial da página
        
        # Capturar screenshot da página inicial
        screenshot_inicial = capturar_screenshot(driver, "tc005_pagina_inicial")
        resultado["screenshots"].append(screenshot_inicial)
        
        # Dados para preencher o formulário
        dados_formulario = {
            "first-name": "João",
            "last-name": "Silva",
            "job-title": "Engenheiro de Testes",
            "education": "College",  # Opções: High School, College, Grad School
            "sex": "Male",  # Opções: Male, Female
            "experience": "2-4",  # Opções: 0-1, 2-4, 5-9, 10+
            "date": "01/01/2025"
        }
        resultado["dados_formulario"] = dados_formulario
        
        # Passo 1: Preencher nome e sobrenome
        try:
            # Preencher primeiro nome
            campo_primeiro_nome = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "first-name"))
            )
            campo_primeiro_nome.send_keys(dados_formulario["first-name"])
            resultado["mensagens"].append(f"Preencheu primeiro nome: {dados_formulario['first-name']}")
            
            # Preencher sobrenome
            campo_sobrenome = driver.find_element(By.ID, "last-name")
            campo_sobrenome.send_keys(dados_formulario["last-name"])
            resultado["mensagens"].append(f"Preencheu sobrenome: {dados_formulario['last-name']}")
            
            # Preencher cargo
            campo_cargo = driver.find_element(By.ID, "job-title")
            campo_cargo.send_keys(dados_formulario["job-title"])
            resultado["mensagens"].append(f"Preencheu cargo: {dados_formulario['job-title']}")
        except Exception as e:
            resultado["mensagens"].append(f"Erro ao preencher dados pessoais: {str(e)}")
        
        # Passo 2: Selecionar nível de educação (radio button)
        try:
            # Mapear opções de educação para seus IDs
            educacao_opcoes = {
                "High School": "radio-button-1",
                "College": "radio-button-2",
                "Grad School": "radio-button-3"
            }
            
            # Selecionar a opção de educação
            if dados_formulario["education"] in educacao_opcoes:
                radio_educacao = driver.find_element(By.ID, educacao_opcoes[dados_formulario["education"]])
                radio_educacao.click()
                resultado["mensagens"].append(f"Selecionou nível de educação: {dados_formulario['education']}")
            else:
                resultado["mensagens"].append(f"Opção de educação inválida: {dados_formulario['education']}")
        except Exception as e:
            resultado["mensagens"].append(f"Erro ao selecionar nível de educação: {str(e)}")
        
        # Passo 3: Selecionar sexo (radio button)
        try:
            # Mapear opções de sexo para seus IDs
            sexo_opcoes = {
                "Male": "radio-button-male",
                "Female": "radio-button-female"
            }
            
            # Selecionar a opção de sexo
            if dados_formulario["sex"] in sexo_opcoes:
                radio_sexo = driver.find_element(By.CSS_SELECTOR, f"input[value='{dados_formulario['sex']}']")
                radio_sexo.click()
                resultado["mensagens"].append(f"Selecionou sexo: {dados_formulario['sex']}")
            else:
                resultado["mensagens"].append(f"Opção de sexo inválida: {dados_formulario['sex']}")
        except Exception as e:
            resultado["mensagens"].append(f"Erro ao selecionar sexo: {str(e)}")
        
        # Passo 4: Selecionar anos de experiência (checkbox)
        try:
            # Mapear opções de experiência para seus IDs
            experiencia_opcoes = {
                "0-1": "checkbox-1",
                "2-4": "checkbox-2",
                "5-9": "checkbox-3",
                "10+": "checkbox-4"
            }
            
            # Selecionar a opção de experiência
            if dados_formulario["experience"] in experiencia_opcoes:
                checkbox_experiencia = driver.find_element(By.ID, experiencia_opcoes[dados_formulario["experience"]])
                checkbox_experiencia.click()
                resultado["mensagens"].append(f"Selecionou anos de experiência: {dados_formulario['experience']}")
            else:
                resultado["mensagens"].append(f"Opção de experiência inválida: {dados_formulario['experience']}")
        except Exception as e:
            resultado["mensagens"].append(f"Erro ao selecionar anos de experiência: {str(e)}")
        
        # Passo 5: Preencher data
        try:
            campo_data = driver.find_element(By.ID, "datepicker")
            campo_data.send_keys(dados_formulario["date"])
            resultado["mensagens"].append(f"Preencheu data: {dados_formulario['date']}")
            
            # Clicar fora do campo de data para fechar o calendário, se aberto
            driver.find_element(By.TAG_NAME, "body").click()
        except Exception as e:
            resultado["mensagens"].append(f"Erro ao preencher data: {str(e)}")
        
        # Capturar screenshot do formulário preenchido
        screenshot_form = capturar_screenshot(driver, "tc005_formulario_preenchido")
        resultado["screenshots"].append(screenshot_form)
        
        # Passo 6: Submeter o formulário
        try:
            botao_submit = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-lg.btn-primary"))
            )
            botao_submit.click()
            resultado["mensagens"].append("Clicou no botão Submit")
            time.sleep(2)  # Aguardar processamento do formulário
        except Exception as e:
            resultado["mensagens"].append(f"Erro ao submeter o formulário: {str(e)}")
        
        # Passo 7: Verificar mensagem de sucesso
        try:
            # Aguardar a exibição da mensagem de sucesso
            mensagem_sucesso = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert.alert-success"))
            )
            
            texto_sucesso = mensagem_sucesso.text
            resultado["mensagens"].append(f"Mensagem após submissão: {texto_sucesso}")
            
            # Capturar screenshot da mensagem de sucesso
            screenshot_sucesso = capturar_screenshot(driver, "tc005_mensagem_sucesso")
            resultado["screenshots"].append(screenshot_sucesso)
            
            # Verificar se a mensagem contém texto de sucesso
            if "success" in texto_sucesso.lower() or "submitted" in texto_sucesso.lower():
                resultado["status"] = "Passou"
                resultado["mensagens"].append("Teste passou: Formulário submetido com sucesso e mensagem de confirmação exibida.")
            else:
                resultado["status"] = "Falhou"
                resultado["mensagens"].append(f"Teste falhou: Mensagem de sucesso não encontrada. Texto exibido: {texto_sucesso}")
        except TimeoutException:
            resultado["status"] = "Falhou"
            resultado["mensagens"].append("Teste falhou: Timeout ao aguardar mensagem de sucesso após submissão do formulário.")
        except Exception as e:
            resultado["status"] = "Falhou"
            resultado["mensagens"].append(f"Erro ao verificar mensagem de sucesso: {str(e)}")
    
    except Exception as e:
        resultado["status"] = "Falhou"
        resultado["mensagens"].append(f"Erro durante a execução do teste: {str(e)}")
    
    finally:
        # Registrar fim do teste
        if driver:
            # Capturar screenshot final, independente do resultado
            screenshot_final = capturar_screenshot(driver, "tc005_final")
            resultado["screenshots"].append(screenshot_final)
            
            # Fechar o driver
            driver.quit()
            resultado["mensagens"].append("Driver fechado.")
        
        # Registrar tempo de execução
        resultado["fim"], resultado["duracao"] = registrar_fim_teste("TC-005: Formy - Preenchimento de Formulário", resultado["inicio"])
    
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
        
        f.write(f"## Dados do Formulário\n")
        for campo, valor in resultado['dados_formulario'].items():
            f.write(f"- **{campo}**: {valor}\n")
        
        f.write(f"\n## Passos Executados\n")
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
    
    # Executar TC-005: Formy - Preenchimento de Formulário
    resultado_tc005 = executar_tc005_formy_formulario()
    arquivo_resultado_tc005 = os.path.join(resultados_dir, "resultado_tc005.md")
    salvar_resultado_para_relatorio(resultado_tc005, arquivo_resultado_tc005)
    print(f"Resultado do TC-005 salvo em: {arquivo_resultado_tc005}")
    
    # Imprimir resumo dos resultados
    print("\nResumo dos Resultados:")
    print(f"TC-005: {resultado_tc005['status']}")
