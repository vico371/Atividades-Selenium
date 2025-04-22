"""
Teste automatizado para o site The Internet Herokuapp - Dynamic Loading.
Este script implementa o caso de teste TC-003 para o site Dynamic Loading.

TC-003: Ao clicar no botão Start, aguardar até o texto "Hello World!" estar visível e validar sua presença.
"""
import sys
import os
import time
from datetime import datetime

# Adicionar o diretório pai ao path para importar o módulo config_base
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from config_base import configurar_driver, registrar_inicio_teste, registrar_fim_teste, capturar_screenshot

# Importar classes específicas para espera explícita
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# URL do site
URL = "https://the-internet.herokuapp.com/dynamic_loading/1"  # Usando o exemplo 1

def executar_tc003_dynamic_loading():
    """
    TC-003: Teste de carregamento dinâmico - aguardar até o texto "Hello World!" estar visível.
    
    Returns:
        dict: Resultado do teste contendo status, mensagens e caminhos para screenshots.
    """
    # Inicializar resultado do teste
    resultado = {
        "id": "TC-003",
        "descricao": "Aguardar carregamento dinâmico de texto",
        "status": "Falhou",
        "mensagens": [],
        "screenshots": [],
        "inicio": None,
        "fim": None,
        "duracao": None,
        "tempo_espera": None
    }
    
    # Registrar início do teste
    resultado["inicio"] = registrar_inicio_teste("TC-003: Dynamic Loading")
    
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
        screenshot_inicial = capturar_screenshot(driver, "tc003_pagina_inicial")
        resultado["screenshots"].append(screenshot_inicial)
        
        # Localizar e clicar no botão Start
        start_button = driver.find_element(By.CSS_SELECTOR, "div#start button")
        start_button.click()
        resultado["mensagens"].append("Clicou no botão Start")
        
        # Capturar screenshot após clicar no botão
        screenshot_apos_clique = capturar_screenshot(driver, "tc003_apos_clique")
        resultado["screenshots"].append(screenshot_apos_clique)
        
        # Registrar tempo antes de iniciar a espera
        tempo_inicio_espera = time.time()
        
        # Aguardar até que o elemento com o texto "Hello World!" esteja visível
        # Usando espera explícita com timeout de 30 segundos
        try:
            # Aguardar o desaparecimento do loading
            WebDriverWait(driver, 10).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, "div#loading"))
            )
            resultado["mensagens"].append("Loading desapareceu")
            
            # Aguardar a visibilidade do elemento com o texto
            elemento_hello = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div#finish h4"))
            )
            
            # Calcular o tempo de espera
            tempo_fim_espera = time.time()
            resultado["tempo_espera"] = tempo_fim_espera - tempo_inicio_espera
            resultado["mensagens"].append(f"Tempo de espera: {resultado['tempo_espera']:.2f} segundos")
            
            # Verificar se o texto é "Hello World!"
            texto_elemento = elemento_hello.text
            resultado["mensagens"].append(f"Texto encontrado: '{texto_elemento}'")
            
            if texto_elemento == "Hello World!":
                resultado["status"] = "Passou"
                resultado["mensagens"].append("Teste passou: Texto 'Hello World!' encontrado após carregamento dinâmico.")
            else:
                resultado["status"] = "Falhou"
                resultado["mensagens"].append(f"Teste falhou: Texto encontrado '{texto_elemento}' não corresponde ao esperado 'Hello World!'")
            
            # Capturar screenshot do texto carregado
            screenshot_texto = capturar_screenshot(driver, "tc003_texto_carregado")
            resultado["screenshots"].append(screenshot_texto)
            
        except TimeoutException:
            resultado["status"] = "Falhou"
            resultado["mensagens"].append("Teste falhou: Timeout ao aguardar o texto 'Hello World!'")
            
            # Capturar screenshot do timeout
            screenshot_timeout = capturar_screenshot(driver, "tc003_timeout")
            resultado["screenshots"].append(screenshot_timeout)
    
    except Exception as e:
        resultado["status"] = "Falhou"
        resultado["mensagens"].append(f"Erro durante a execução do teste: {str(e)}")
    
    finally:
        # Registrar fim do teste
        if driver:
            # Capturar screenshot final, independente do resultado
            screenshot_final = capturar_screenshot(driver, "tc003_final")
            resultado["screenshots"].append(screenshot_final)
            
            # Fechar o driver
            driver.quit()
            resultado["mensagens"].append("Driver fechado.")
        
        # Registrar tempo de execução
        resultado["fim"], resultado["duracao"] = registrar_fim_teste("TC-003: Dynamic Loading", resultado["inicio"])
    
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
        f.write(f"- **Duração**: {resultado['duracao']:.2f} segundos\n")
        if resultado['tempo_espera']:
            f.write(f"- **Tempo de Espera para Carregamento**: {resultado['tempo_espera']:.2f} segundos\n\n")
        else:
            f.write("\n")
        
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
    
    # Executar TC-003: Dynamic Loading
    resultado_tc003 = executar_tc003_dynamic_loading()
    arquivo_resultado_tc003 = os.path.join(resultados_dir, "resultado_tc003.md")
    salvar_resultado_para_relatorio(resultado_tc003, arquivo_resultado_tc003)
    print(f"Resultado do TC-003 salvo em: {arquivo_resultado_tc003}")
    
    # Imprimir resumo dos resultados
    print("\nResumo dos Resultados:")
    print(f"TC-003: {resultado_tc003['status']}")
    if resultado_tc003['tempo_espera']:
        print(f"Tempo de espera: {resultado_tc003['tempo_espera']:.2f} segundos")
