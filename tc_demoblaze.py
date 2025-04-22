"""
Teste automatizado para o site DemoBlaze.
Este script implementa o caso de teste TC-004 para o site DemoBlaze.

TC-004: Simular uma compra de um produto qualquer.
"""
import sys
import os
import time
from datetime import datetime
import random

# Adicionar o diretório pai ao path para importar o módulo config_base
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from config_base import configurar_driver, registrar_inicio_teste, registrar_fim_teste, capturar_screenshot

# Importar classes específicas para espera explícita e tratamento de alertas
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoAlertPresentException

# URL do site
URL = "https://www.demoblaze.com/"

def executar_tc004_demoblaze_compra():
    """
    TC-004: Teste de simulação de compra de um produto no site DemoBlaze.
    
    Returns:
        dict: Resultado do teste contendo status, mensagens e caminhos para screenshots.
    """
    # Inicializar resultado do teste
    resultado = {
        "id": "TC-004",
        "descricao": "Simulação de compra de produto",
        "status": "Falhou",
        "mensagens": [],
        "screenshots": [],
        "inicio": None,
        "fim": None,
        "duracao": None,
        "dados_compra": {
            "produto": None,
            "preco": None,
            "id_pedido": None,
            "valor_total": None,
            "dados_cliente": {}
        }
    }
    
    # Registrar início do teste
    resultado["inicio"] = registrar_inicio_teste("TC-004: DemoBlaze - Compra de Produto")
    
    # Configurar driver
    driver = None
    try:
        driver = configurar_driver()
        resultado["mensagens"].append("Driver configurado com sucesso.")
        
        # Navegar para a página
        driver.get(URL)
        resultado["mensagens"].append(f"Navegou para {URL}")
        time.sleep(3)  # Aguardar carregamento inicial da página
        
        # Capturar screenshot da página inicial
        screenshot_inicial = capturar_screenshot(driver, "tc004_pagina_inicial")
        resultado["screenshots"].append(screenshot_inicial)
        
        # Passo 1: Escolher um produto aleatório da lista
        # Aguardar carregamento dos produtos
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".card-block"))
        )
        
        # Obter lista de produtos
        produtos = driver.find_elements(By.CSS_SELECTOR, ".card-title")
        if not produtos:
            raise Exception("Nenhum produto encontrado na página")
        
        # Escolher um produto aleatório
        produto_aleatorio = random.choice(produtos)
        nome_produto = produto_aleatorio.text
        resultado["dados_compra"]["produto"] = nome_produto
        resultado["mensagens"].append(f"Produto escolhido: {nome_produto}")
        
        # Clicar no produto escolhido
        produto_aleatorio.click()
        resultado["mensagens"].append(f"Clicou no produto: {nome_produto}")
        time.sleep(2)  # Aguardar carregamento da página do produto
        
        # Capturar screenshot da página do produto
        screenshot_produto = capturar_screenshot(driver, "tc004_pagina_produto")
        resultado["screenshots"].append(screenshot_produto)
        
        # Passo 2: Obter o preço do produto
        try:
            preco_elemento = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".price-container"))
            )
            preco_texto = preco_elemento.text
            # Extrair apenas o valor numérico do preço (remover "$" e outros caracteres)
            preco = ''.join(filter(lambda x: x.isdigit() or x == '.', preco_texto))
            resultado["dados_compra"]["preco"] = preco
            resultado["mensagens"].append(f"Preço do produto: ${preco}")
        except Exception as e:
            resultado["mensagens"].append(f"Não foi possível obter o preço do produto: {str(e)}")
        
        # Passo 3: Adicionar ao carrinho
        try:
            botao_add = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-success"))
            )
            botao_add.click()
            resultado["mensagens"].append("Clicou em 'Add to cart'")
            
            # Aguardar e aceitar o alerta
            try:
                WebDriverWait(driver, 5).until(EC.alert_is_present())
                alerta = driver.switch_to.alert
                texto_alerta = alerta.text
                resultado["mensagens"].append(f"Alerta exibido: {texto_alerta}")
                alerta.accept()
                resultado["mensagens"].append("Alerta aceito")
            except NoAlertPresentException:
                resultado["mensagens"].append("Nenhum alerta foi exibido após adicionar ao carrinho")
        except Exception as e:
            resultado["mensagens"].append(f"Erro ao adicionar produto ao carrinho: {str(e)}")
        
        # Passo 4: Ir para o carrinho
        try:
            # Aguardar um pouco para garantir que o alerta foi processado
            time.sleep(2)
            
            link_cart = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "cartur"))
            )
            link_cart.click()
            resultado["mensagens"].append("Navegou para o carrinho")
            time.sleep(2)  # Aguardar carregamento da página do carrinho
            
            # Capturar screenshot do carrinho
            screenshot_cart = capturar_screenshot(driver, "tc004_carrinho")
            resultado["screenshots"].append(screenshot_cart)
        except Exception as e:
            resultado["mensagens"].append(f"Erro ao navegar para o carrinho: {str(e)}")
        
        # Passo 5: Clicar em Place Order
        try:
            botao_order = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-success"))
            )
            botao_order.click()
            resultado["mensagens"].append("Clicou em 'Place Order'")
            time.sleep(2)  # Aguardar abertura do modal
            
            # Capturar screenshot do modal de pedido
            screenshot_modal = capturar_screenshot(driver, "tc004_modal_pedido")
            resultado["screenshots"].append(screenshot_modal)
        except Exception as e:
            resultado["mensagens"].append(f"Erro ao clicar em 'Place Order': {str(e)}")
        
        # Passo 6: Preencher o formulário de pedido
        try:
            # Dados do cliente para o formulário
            dados_cliente = {
                "name": "Cliente Teste",
                "country": "Brasil",
                "city": "São Paulo",
                "card": "4111111111111111",
                "month": "12",
                "year": "2025"
            }
            resultado["dados_compra"]["dados_cliente"] = dados_cliente
            
            # Preencher nome
            campo_nome = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "name"))
            )
            campo_nome.send_keys(dados_cliente["name"])
            
            # Preencher país
            campo_pais = driver.find_element(By.ID, "country")
            campo_pais.send_keys(dados_cliente["country"])
            
            # Preencher cidade
            campo_cidade = driver.find_element(By.ID, "city")
            campo_cidade.send_keys(dados_cliente["city"])
            
            # Preencher cartão
            campo_cartao = driver.find_element(By.ID, "card")
            campo_cartao.send_keys(dados_cliente["card"])
            
            # Preencher mês
            campo_mes = driver.find_element(By.ID, "month")
            campo_mes.send_keys(dados_cliente["month"])
            
            # Preencher ano
            campo_ano = driver.find_element(By.ID, "year")
            campo_ano.send_keys(dados_cliente["year"])
            
            resultado["mensagens"].append("Preencheu o formulário de pedido com os dados do cliente")
            
            # Capturar screenshot do formulário preenchido
            screenshot_form = capturar_screenshot(driver, "tc004_formulario_preenchido")
            resultado["screenshots"].append(screenshot_form)
        except Exception as e:
            resultado["mensagens"].append(f"Erro ao preencher o formulário de pedido: {str(e)}")
        
        # Passo 7: Confirmar a compra
        try:
            botao_purchase = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#orderModal .btn-primary"))
            )
            botao_purchase.click()
            resultado["mensagens"].append("Clicou em 'Purchase'")
            time.sleep(2)  # Aguardar processamento da compra
            
            # Capturar screenshot da confirmação
            screenshot_confirm = capturar_screenshot(driver, "tc004_confirmacao_compra")
            resultado["screenshots"].append(screenshot_confirm)
        except Exception as e:
            resultado["mensagens"].append(f"Erro ao confirmar a compra: {str(e)}")
        
        # Passo 8: Validar a mensagem de confirmação
        try:
            # Aguardar a exibição da mensagem de confirmação
            confirmacao = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".sweet-alert"))
            )
            
            # Obter o texto completo da confirmação
            texto_confirmacao = confirmacao.text
            resultado["mensagens"].append(f"Mensagem de confirmação: {texto_confirmacao}")
            
            # Extrair ID do pedido e valor total
            if "Id:" in texto_confirmacao and "Amount:" in texto_confirmacao:
                linhas = texto_confirmacao.split('\n')
                for linha in linhas:
                    if "Id:" in linha:
                        resultado["dados_compra"]["id_pedido"] = linha.split("Id:")[1].strip()
                    if "Amount:" in linha:
                        resultado["dados_compra"]["valor_total"] = linha.split("Amount:")[1].strip()
                
                resultado["mensagens"].append(f"ID do Pedido: {resultado['dados_compra']['id_pedido']}")
                resultado["mensagens"].append(f"Valor Total: {resultado['dados_compra']['valor_total']}")
                
                # Se chegou até aqui, o teste passou
                resultado["status"] = "Passou"
                resultado["mensagens"].append("Teste passou: Compra realizada com sucesso e confirmação recebida.")
            else:
                resultado["status"] = "Falhou"
                resultado["mensagens"].append("Teste falhou: Não foi possível extrair ID do pedido e valor total da confirmação.")
        except Exception as e:
            resultado["status"] = "Falhou"
            resultado["mensagens"].append(f"Erro ao validar a mensagem de confirmação: {str(e)}")
    
    except Exception as e:
        resultado["status"] = "Falhou"
        resultado["mensagens"].append(f"Erro durante a execução do teste: {str(e)}")
    
    finally:
        # Registrar fim do teste
        if driver:
            # Capturar screenshot final, independente do resultado
            screenshot_final = capturar_screenshot(driver, "tc004_final")
            resultado["screenshots"].append(screenshot_final)
            
            # Fechar o driver
            driver.quit()
            resultado["mensagens"].append("Driver fechado.")
        
        # Registrar tempo de execução
        resultado["fim"], resultado["duracao"] = registrar_fim_teste("TC-004: DemoBlaze - Compra de Produto", resultado["inicio"])
    
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
        
        f.write(f"## Dados da Compra\n")
        f.write(f"- **Produto**: {resultado['dados_compra']['produto']}\n")
        if resultado['dados_compra']['preco']:
            f.write(f"- **Preço do Produto**: ${resultado['dados_compra']['preco']}\n")
        if resultado['dados_compra']['id_pedido']:
            f.write(f"- **ID do Pedido**: {resultado['dados_compra']['id_pedido']}\n")
        if resultado['dados_compra']['valor_total']:
            f.write(f"- **Valor Total**: {resultado['dados_compra']['valor_total']}\n")
        
        f.write(f"\n## Dados do Cliente\n")
        for chave, valor in resultado['dados_compra']['dados_cliente'].items():
            f.write(f"- **{chave.capitalize()}**: {valor}\n")
        
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
    
    # Executar TC-004: DemoBlaze - Compra de Produto
    resultado_tc004 = executar_tc004_demoblaze_compra()
    arquivo_resultado_tc004 = os.path.join(resultados_dir, "resultado_tc004.md")
    salvar_resultado_para_relatorio(resultado_tc004, arquivo_resultado_tc004)
    print(f"Resultado do TC-004 salvo em: {arquivo_resultado_tc004}")
    
    # Imprimir resumo dos resultados
    print("\nResumo dos Resultados:")
    print(f"TC-004: {resultado_tc004['status']}")
    if resultado_tc004['dados_compra']['id_pedido']:
        print(f"ID do Pedido: {resultado_tc004['dados_compra']['id_pedido']}")
    if resultado_tc004['dados_compra']['valor_total']:
        print(f"Valor Total: {resultado_tc004['dados_compra']['valor_total']}")

