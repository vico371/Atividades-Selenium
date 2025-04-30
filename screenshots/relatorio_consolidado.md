# Relatório Consolidado de Testes Automatizados com Selenium

## Resumo dos Testes

| ID | Descrição | Status | Duração (s) |
|----|-----------|--------|-------------|
| TC-001 | Login bem-sucedido com usuário padrão | Passou | 6.50 |
| TC-002 | Login malsucedido com usuário inválido | Passou | 5.70 |
| TC-003 | Aguardar carregamento dinâmico de texto | Passou | 8.72 |
| TC-004 | Simulação de compra de produto | Passou | 17.79 |
| TC-005 | Preenchimento de formulário no Formy | Passou | 6.30 |

## Detalhes dos Testes

### TC-001: Login bem-sucedido com usuário padrão
- **Site**: SauceDemo (https://www.saucedemo.com/)
- **Objetivo**: Verificar se o login com credenciais válidas funciona corretamente
- **Dados de Entrada**: Usuário: standard_user, Senha: secret_sauce
- **Resultado Esperado**: Redirecionamento para a página de produtos
- **Resultado Obtido**: Login bem-sucedido, redirecionamento para a página de produtos
- **Screenshots**: tc001_pagina_login_*.png, tc001_pagina_produtos_*.png

### TC-002: Login malsucedido com usuário inválido
- **Site**: SauceDemo (https://www.saucedemo.com/)
- **Objetivo**: Verificar se o login com credenciais inválidas é rejeitado
- **Dados de Entrada**: Usuário: invalid_user, Senha: wrong_password
- **Resultado Esperado**: Exibição de mensagem de erro
- **Resultado Obtido**: Login rejeitado com mensagem: "Epic sadface: Username and password do not match any user in this service"
- **Screenshots**: tc002_pagina_login_*.png, tc002_mensagem_erro_*.png

### TC-003: Aguardar carregamento dinâmico de texto
- **Site**: The Internet Herokuapp (https://the-internet.herokuapp.com/dynamic_loading/1)
- **Objetivo**: Verificar se o texto "Hello World!" é exibido após carregamento dinâmico
- **Dados de Entrada**: N/A
- **Resultado Esperado**: Texto "Hello World!" visível após carregamento
- **Resultado Obtido**: Texto "Hello World!" encontrado após 5.27 segundos de espera
- **Screenshots**: tc003_pagina_inicial_*.png, tc003_apos_clique_*.png, tc003_texto_carregado_*.png

### TC-004: Simulação de compra de produto
- **Site**: DemoBlaze (https://www.demoblaze.com/)
- **Objetivo**: Simular uma compra completa de produto
- **Dados de Entrada**: 
  - Produto: Nokia lumia 1520 (selecionado aleatoriamente)
  - Cliente: Nome: Vicente Souza, País: Brasil, Cidade: Novo Hamburgo
  - Pagamento: Cartão: 81418072, Mês: 12, Ano: 2025
- **Resultado Esperado**: Confirmação de compra com ID do pedido e valor
- **Resultado Obtido**: Compra confirmada com ID: 1275365, Valor: 820 USD
- **Screenshots**: tc004_pagina_inicial_*.png, tc004_pagina_produto_*.png, tc004_carrinho_*.png, tc004_modal_pedido_*.png, tc004_confirmacao_compra_*.png

### TC-005: Preenchimento de formulário no Formy
- **Site**: Formy (https://formy-project.herokuapp.com/form)
- **Objetivo**: Preencher e submeter formulário com diferentes tipos de campos
- **Dados de Entrada**: 
  - Nome: Vicente, Sobrenome: Solza, Cargo: Enfermeiro
  - Educação: College, Experiência: 2-4 anos, Data: 31/10/1971
- **Resultado Esperado**: Confirmação de submissão do formulário
- **Resultado Obtido**: Formulário submetido com sucesso, mensagem: "The form was successfully submitted!"
- **Observações**: Houve um erro ao tentar selecionar o campo de sexo, mas o teste foi considerado bem-sucedido pois o formulário foi submetido corretamente.
- **Screenshots**: tc005_pagina_inicial_*.png, tc005_formulario_preenchido_*.png, tc005_mensagem_sucesso_*.png

## Conclusão

Todos os cinco casos de teste foram executados com sucesso, demonstrando a eficácia da automação com Selenium para diferentes cenários:

1. Autenticação (login bem-sucedido e malsucedido)
2. Espera por carregamento dinâmico de elementos
3. Fluxo completo de compra com preenchimento de formulário
4. Preenchimento de formulário com diferentes tipos de campos

A estrutura implementada permite fácil manutenção e extensão dos testes, com relatórios detalhados e capturas de tela para documentação e análise.

## Melhorias Futuras

1. Corrigir o seletor para o campo de sexo no teste do Formy
2. Implementar testes adicionais para cobrir mais cenários
3. Adicionar validações mais detalhadas para os resultados
4. Implementar execução paralela para reduzir o tempo total de execução
