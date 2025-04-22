# Relatório de Teste: TC-005 - Preenchimento de formulário no Formy

## Informações Gerais
- **ID do Teste**: TC-005
- **Descrição**: Preenchimento de formulário no Formy
- **Status**: Passou
- **Data/Hora de Início**: 2025-04-20 15:40:01.109571
- **Data/Hora de Término**: 2025-04-20 15:40:07.411519
- **Duração**: 6.30 segundos

## Dados do Formulário
- **first-name**: João
- **last-name**: Silva
- **job-title**: Engenheiro de Testes
- **education**: College
- **sex**: Male
- **experience**: 2-4
- **date**: 01/01/2025

## Passos Executados
1. Driver configurado com sucesso.
2. Navegou para https://formy-project.herokuapp.com/form
3. Preencheu primeiro nome: vicente 
4. Preencheu sobrenome: Souza
5. Preencheu cargo: Enfermeiro
6. Selecionou nível de educação: faculty
7. Erro ao selecionar sexo: Message: no such element: Unable to locate element: {"method":"css selector","selector":"input[value='Male']"}
  (Session info: chrome=135.0.7049.84); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#no-such-element-exception
Stacktrace:
#0 0x560ce928acea <unknown>
#1 0x560ce8d3b5f0 <unknown>
#2 0x560ce8d8ca33 <unknown>
#3 0x560ce8d8cc21 <unknown>
#4 0x560ce8ddb274 <unknown>
#5 0x560ce8db268d <unknown>
#6 0x560ce8dd8660 <unknown>
#7 0x560ce8db2433 <unknown>
#8 0x560ce8d7eea3 <unknown>
#9 0x560ce8d7fb01 <unknown>
#10 0x560ce924fb3b <unknown>
#11 0x560ce9253a21 <unknown>
#12 0x560ce9236c32 <unknown>
#13 0x560ce9254594 <unknown>
#14 0x560ce921aeef <unknown>
#15 0x560ce9278d98 <unknown>
#16 0x560ce9278f76 <unknown>
#17 0x560ce9289b36 <unknown>
#18 0x7f19a9c94ac3 <unknown>

8. Selecionou anos de experiência: 2-4
9. Preencheu data: 31/10/2025
10. Clicou no botão Submit
11. Mensagem após submissão: The form was successfully submitted!
12. Teste passou: Formulário submetido com sucesso e mensagem de confirmação exibida.
13. Driver fechado.

## Screenshots
- tc005_pagina_inicial_20250420_154003.png
- tc005_formulario_preenchido_20250420_154004.png
- tc005_mensagem_sucesso_20250420_154007.png
- tc005_final_20250420_154007.png
