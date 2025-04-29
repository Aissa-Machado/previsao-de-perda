import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib

#lendo arquivo csv
df = pd.read_csv('data/base_cancelamento_clientes.csv')
#entradas e saidas para treinar a IA
entradas = df[['tempo_uso_meses','numero_reclamacoes','atrasos_pagamento','usou_suporte']]
saida = df['cancelou']
#separar treino e teste
entradas_train, entradas_test,saida_train,saida_test = train_test_split(entradas,saida,test_size=0.3, random_state=42)
#criar modelo
modelo = DecisionTreeClassifier()
#treinar modelo
modelo.fit(entradas_train, saida_train)
#fazer previsoes
previsoes = modelo.predict(entradas_test)
#avaliar
precisao = accuracy_score(saida_test,previsoes)
print(f'A precisao foi de {precisao*100:.2f} %')
print('Previsoẽs', previsoes)
print('Respostas corretas', saida_test)

novos_clientes = pd.read_csv('data/novos_clientes_para_prever.csv')
entrada_novos_cliente = novos_clientes[['tempo_uso_meses','numero_reclamacoes','atrasos_pagamento','usou_suporte']]
previsoes_novos_cliente = modelo.predict(entrada_novos_cliente)
novos_clientes['previsao_cancelamento'] = previsoes_novos_cliente
novos_clientes.to_csv('data/novos_clientes_para_prever_feito')
print('Abra o arquivo "novos_clientes_para_prever_feito.csv" para verificar a previsão de cancelmaneto dos clientes!')