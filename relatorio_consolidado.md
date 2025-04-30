Relatório Consolidado de Testes Automatizados com Selenium
Resumo dos Testes
ID	Descrição	Status	Duração (s)
TC-001	Login bem-sucedido com usuário padrão	 Passou	6.50
TC-002	Login malsucedido com usuário inválido	 Passou	5.70
TC-003	Aguardar carregamento dinâmico de texto	 Passou	8.72
TC-004	Simulação de compra de produto	 Passou	17.79
TC-005	Preenchimento de formulário no Formy	 Passou	6.30
Detalhes dos Testes

**TC-001: Login bem-sucedido com usuário padrão
Site: SauceDemo

Objetivo: Verificar se o login com credenciais válidas funciona corretamente.

Dados usados:

Usuário: standard_user

Senha: secret_sauce

Resultado esperado: Redirecionamento para a página de produtos.

O que aconteceu:

O login foi bem-sucedido e fui redirecionado para a página de produtos.

Capturas: tc001_pagina_login_*.png, tc001_pagina_produtos_*.png.

 TC-002: Login malsucedido com usuário inválido
Site: SauceDemo

Objetivo: Verificar se o login falha com credenciais inválidas.

Dados usados:

Usuário: invalid_user

Senha: wrong_password

Resultado esperado: Mensagem de erro deve aparecer.

O que aconteceu:

O sistema exibiu a mensagem:

"Epic sadface: Username and password do not match any user in this service"

Capturas: tc002_pagina_login_*.png, tc002_mensagem_erro_*.png.

** TC-003: Aguardar carregamento dinâmico de texto
Site: The Internet Herokuapp

Objetivo: Verificar se o texto "Hello World!" aparece após carregamento dinâmico.

O que aconteceu:

O texto "Hello World!" foi exibido após 5.27 segundos de espera.

Capturas: tc003_pagina_inicial_*.png, tc003_apos_clique_*.png, tc003_texto_carregado_*.png.

** TC-004: Simulação de compra de produto
Site: DemoBlaze

Objetivo: Simular uma compra completa.

Dados usados:

Produto: Nokia Lumia 1520 (selecionado aleatoriamente)

Cliente:

Nome: Vicente Souza

País: Brasil

Cidade: Novo Hamburgo

Pagamento:

Cartão: 81418072

Mês: 12

Ano: 2025

Resultado esperado: Confirmação da compra com ID e valor.

O que aconteceu:

Compra confirmada com ID: 1275365 e Valor: 820 USD.

Capturas: tc004_pagina_inicial_*.png, tc004_pagina_produto_*.png, tc004_carrinho_*.png, tc004_confirmacao_compra_*.png.

 **TC-005: Preenchimento de formulário no Formy
Site: Formy

Objetivo: Preencher e submeter um formulário complexo.

Dados usados:

Nome: Vicente

Sobrenome: Solza

Cargo: Enfermeiro

Educação: College

Experiência: 2-4 anos

Data: 31/10/1971

Resultado esperado: Mensagem de sucesso após envio.

O que aconteceu:

O formulário foi submetido com sucesso!

Mensagem exibida:

"The form was successfully submitted!"

Observação: Tive um pequeno problema ao selecionar o campo de sexo, mas o envio funcionou normalmente.

Capturas: tc005_pagina_inicial_*.png, tc005_formulario_preenchido_*.png, tc005_mensagem_sucesso_*.png.

 Conclusão
Todos os 5 testes automatizados passaram com sucesso! 

O Selenium mostrou-se eficiente para:
✔ Testes de login (sucesso e falha)
✔ Espera por elementos dinâmicos
✔ Simulação de compras (fluxo completo)
✔ Preenchimento de formulários

A estrutura atual permite fácil manutenção e expansão.

 Melhorias Futuras
1️ Corrigir o seletor do campo de sexo no TC-005 (Formy).
2️ Adicionar mais cenários de teste para aumentar a cobertura.
3️ Melhorar validações (ex.: checar dados retornados).
4️ Testes em paralelo para reduzir tempo de execução.

