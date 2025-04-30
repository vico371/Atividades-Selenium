#!/bin/bash


echo "===== Iniciando execução de todos os testes automatizados ====="
echo "Data/Hora: $(date)"
echo

mkdir -p /home/ubuntu/projeto-selenium/logs

echo "Executando testes para SauceDemo (TC-001 e TC-002)..."
cd /home/ubuntu/projeto-selenium/scripts
python3 tc_saucedemo.py > /home/ubuntu/projeto-selenium/logs/log_saucedemo.txt 2>&1
if [ $? -eq 0 ]; then
    echo "✓ Testes SauceDemo executados com sucesso."
else
    echo "✗ Erro na execução dos testes SauceDemo. Verifique o log para mais detalhes."
fi
echo
echo "Executando teste para Dynamic Loading (TC-003)..."
cd /home/ubuntu/projeto-selenium/scripts
python3 tc_dynamic_loading.py > /home/ubuntu/projeto-selenium/logs/log_dynamic_loading.txt 2>&1
if [ $? -eq 0 ]; then
    echo "✓ Teste Dynamic Loading executado com sucesso."
else
    echo "✗ Erro na execução do teste Dynamic Loading. Verifique o log para mais detalhes."
fi
echo
echo "Executando teste para DemoBlaze (TC-004)..."
cd /home/ubuntu/projeto-selenium/scripts
python3 tc_demoblaze.py > /home/ubuntu/projeto-selenium/logs/log_demoblaze.txt 2>&1
if [ $? -eq 0 ]; then
    echo "✓ Teste DemoBlaze executado com sucesso."
else
    echo "✗ Erro na execução do teste DemoBlaze. Verifique o log para mais detalhes."
fi
echo

echo "Executando teste para Formy (TC-005)..."
cd /home/ubuntu/projeto-selenium/scripts
python3 tc_formy.py > /home/ubuntu/projeto-selenium/logs/log_formy.txt 2>&1
if [ $? -eq 0 ]; then
    echo "✓ Teste Formy executado com sucesso."
else
    echo "✗ Erro na execução do teste Formy. Verifique o log para mais detalhes."
fi
echo

echo "===== Execução de todos os testes concluída ====="
echo "Data/Hora: $(date)"
echo "Os resultados detalhados estão disponíveis na pasta 'relatorios'."
echo "Os logs de execução estão disponíveis na pasta 'logs'."
