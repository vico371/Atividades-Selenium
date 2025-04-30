"""
Módulo base para configuração do Selenium WebDriver.
Este módulo fornece funções e classes para configurar o WebDriver do Selenium
de forma padronizada para todos os testes.
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import os

def configurar_driver():
    """
    Configura e retorna uma instância do Chrome WebDriver.
    
    Returns:
        webdriver.Chrome: Uma instância configurada do Chrome WebDriver.
    """
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    #chrome_options.add_argument("--headless") 
    
    service = Service(ChromeDriverManager().install())
    
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    return driver

def registrar_inicio_teste(nome_teste):
    """
    Registra o horário de início de um teste.
    
    Args:
        nome_teste (str): Nome do teste sendo executado.
        
    Returns:
        datetime: O horário de início do teste.
    """
    inicio = datetime.now()
    print(f"[{inicio}] Iniciando teste: {nome_teste}")
    return inicio

def registrar_fim_teste(nome_teste, inicio):
    """
    Registra o horário de término de um teste e calcula a duração.
    
    Args:
        nome_teste (str): Nome do teste executado.
        inicio (datetime): Horário de início do teste.
        
    Returns:
        tuple: (horário de término, duração em segundos)
    """
    fim = datetime.now()
    duracao = (fim - inicio).total_seconds()
    print(f"[{fim}] Finalizando teste: {nome_teste}")
    print(f"Duração: {duracao:.2f} segundos")
    return fim, duracao

def criar_diretorio_screenshots():
    """
    Cria um diretório para armazenar screenshots, se não existir.
    
    Returns:
        str: Caminho para o diretório de screenshots.
    """
    screenshots_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "screenshots")
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)
    return screenshots_dir

def capturar_screenshot(driver, nome_arquivo):
    """
    Captura uma screenshot da página atual.
    
    Args:
        driver (webdriver.Chrome): Instância do WebDriver.
        nome_arquivo (str): Nome base para o arquivo de screenshot.
        
    Returns:
        str: Caminho completo para o arquivo de screenshot salvo.
    """
    screenshots_dir = criar_diretorio_screenshots()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    arquivo = os.path.join(screenshots_dir, f"{nome_arquivo}_{timestamp}.png")
    driver.save_screenshot(arquivo)
    print(f"Screenshot salva em: {arquivo}")
    return arquivo
