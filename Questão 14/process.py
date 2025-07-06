import pandas as pd
import time
import sys

print("--- Iniciando o script de processamento de dados ---")
sys.stdout.flush()

# Simula a leitura de dados
time.sleep(1)
print("Dados lidos com sucesso.")
sys.stdout.flush()

dados = {
    'Produto': ['Produto A', 'Produto B', 'Produto C', 'Produto D'],
    'Vendas_2024': [150, 200, 120, 300],
    'Meta_2024': [130, 180, 150, 280]
}
df = pd.DataFrame(dados)

print("\nDataFrame criado:")
print(df)
sys.stdout.flush()

# Simula um processamento demorado
time.sleep(2)
print("\nProcessando dados...")
df['Atingiu_Meta'] = df['Vendas_2024'] >= df['Meta_2024']
print("Processamento concluído.")
sys.stdout.flush()


time.sleep(1)
print("\n--- Resultado Final do Processamento ---")
print(df)
print("\n--- Script finalizado com sucesso. ---")