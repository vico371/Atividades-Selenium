# README - Projeto de Testes Automatizados com Selenium

Este projeto contém a implementação de testes automatizados utilizando Selenium WebDriver em Python, conforme solicitado na atividade prática.

## Estrutura do Projeto

```
projeto-selenium/
├─ drivers/                # WebDrivers (gerenciados automaticamente pelo webdriver-manager)
├─ scripts/                # Scripts de teste para cada caso de teste
│  ├─ config_base.py       # Módulo base de configuração do WebDriver
│  ├─ tc_saucedemo.py      # Testes para SauceDemo (TC-001 e TC-002)
│  ├─ tc_dynamic_loading.py # Teste para Dynamic Loading (TC-003)
│  ├─ tc_demoblaze.py      # Teste para DemoBlaze (TC-004)
│  └─ tc_formy.py          # Teste para Formy (TC-005)
├─ relatorios/             # Relatórios detalhados de cada teste
│  ├─ resultado_tc001.md   # Relatório do TC-001
│  ├─ resultado_tc002.md   # Relatório do TC-002
│  ├─ resultado_tc003.md   # Relatório do TC-003
│  ├─ resultado_tc004.md   # Relatório do TC-004
│  ├─ resultado_tc005.md   # Relatório do TC-005
│  └─ relatorio_consolidado.md # Relatório consolidado de todos os testes
├─ screenshots/            # Screenshots capturadas durante a execução dos testes
├─ logs/                   # Logs de execução dos testes
├─ executar_testes.sh      # Script para executar todos os testes
└─ todo.md                 # Lista de tarefas do projeto
```

## Casos de Teste Implementados

1. **SauceDemo (TC-001 e TC-002)**
   - TC-001: Login bem-sucedido com usuário padrão
   - TC-002: Login malsucedido com usuário inválido

2. **Dynamic Loading (TC-003)**
   - TC-003: Aguardar carregamento dinâmico do texto "Hello World!"

3. **DemoBlaze (TC-004)**
   - TC-004: Simulação completa de compra de produto

4. **Formy (TC-005)**
   - TC-005: Preenchimento de formulário com diferentes tipos de campos

## Como Executar os Testes

1. Certifique-se de ter Python 3.7+ instalado
2. Instale as dependências:
   ```
   pip install selenium webdriver-manager
   ```
3. Execute o script para rodar todos os testes:
   ```
   ./executar_testes.sh
   ```
   
Ou execute cada teste individualmente:
   ```
   cd scripts
   python3 tc_saucedemo.py
   python3 tc_dynamic_loading.py
   python3 tc_demoblaze.py
   python3 tc_formy.py
   ```

## Relatórios

Os relatórios detalhados de cada teste são gerados automaticamente na pasta `relatorios/`. Um relatório consolidado também está disponível em `relatorios/relatorio_consolidado.md`.

## Screenshots

Screenshots de cada etapa dos testes são capturadas automaticamente e salvas na pasta `screenshots/` com timestamps para facilitar a identificação.

## Observações

- Os testes utilizam o modo headless do Chrome para execução sem interface gráfica
- O WebDriver é gerenciado automaticamente pelo webdriver-manager
- Todos os testes incluem tratamento de exceções e registro detalhado de passos
- Os relatórios incluem informações como duração, status, passos executados e screenshots
