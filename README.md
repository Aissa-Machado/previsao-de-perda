# Previsão de Cancelamento de Clientes (Churn)

Este projeto utiliza **Machine Learning com Python** para prever quais clientes têm maior chance de cancelar um serviço, com base em dados históricos como tempo de uso, número de reclamações, uso do suporte e atrasos no pagamento.

## 📁 Estrutura do Projeto

previsao-de-perda/ │ ├── data/ │ ├── base_cancelamento_clientes.csv │ ├── novos_clientes_para_prever.csv │ └── novos_clientes_para_prever_feito.csv │ ├── src/ │ └── main.py │ ├── requirements.txt └── README.md

## 🔍 Objetivo

Treinar um modelo de classificação para prever cancelamentos de clientes e aplicar esse modelo em novos dados para auxiliar na retenção de clientes.

## ⚙️ Como funciona

1. Carrega os dados reais (`base_cancelamento_clientes.csv`)
2. Treina um modelo de Árvore de Decisão com Scikit-Learn
3. Avalia a acurácia da IA nos dados de teste
4. Aplica o modelo em novos clientes (arquivo sem coluna "cancelou")
5. Exporta as previsões em um novo CSV

## 🧠 Modelo Utilizado

- **DecisionTreeClassifier** do Scikit-Learn

## 📈 Métricas

- Acurácia do modelo é exibida no terminal após o treinamento.

## ▶️ Como executar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/previsao-de-perda.git
cd previsao-de-perda
Ative o ambiente virtual (se ainda não estiver ativo):

python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

Instale as dependências:
pip install -r requirements.txt

Execute o script:
python src/main.py
Verifique o arquivo data/novos_clientes_para_prever_feito.csv para ver as previsões.

📝 Requisitos
Python 3.8+
pandas
scikit-learn
joblib

Tudo listado no requirements.txt

✍️ Autor
Aissa Machado - Projeto pessoal para aprendizado em Ciência de Dados e Machine Learning.

bash
Copy
Edit
