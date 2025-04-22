# Relatório de Teste: TC-002 - Login malsucedido com usuário inválido

## Informações Gerais
- **ID do Teste**: TC-002
- **Descrição**: Login malsucedido com usuário inválido
- **Status**: Passou
- **Data/Hora de Início**: 2025-04-20 15:39:27.911756
- **Data/Hora de Término**: 2025-04-20 15:39:33.616547
- **Duração**: 5.70 segundos

## Passos Executados
1. Driver configurado com sucesso.
2. Navegou para https://www.saucedemo.com/
3. Preencheu credenciais inválidas: usuário=invalid_user, senha=wrong_password
4. Clicou no botão de login
5. Mensagem de erro exibida: Epic sadface: Username and password do not match any user in this service
6. Teste passou: Login falhou conforme esperado e exibiu mensagem de erro.
7. Driver fechado.

## Screenshots
- tc002_pagina_login_20250420_153930.png
- tc002_mensagem_erro_20250420_153933.png
- tc002_final_20250420_153933.png
