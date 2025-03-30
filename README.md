# API-de-Operadoras-de-Saude

📦 Pré-requisitos
Python 3.8+ instalado

Git (opcional, para clonar o repositório)

Postman ou similar (para testar os endpoints)

🚀 Instalação Rápida
1. Clone o repositório (ou baixe os arquivos)
git clone https://github.com/seu-usuario/api-operadoras-saude.git
cd api-operadoras-saude

2. Crie e ative um ambiente virtual (recomendado)
python -m venv venv
# No Windows:
venv\Scripts\activate
# No Mac/Linux:
source venv/bin/activate

3. Instale as dependências
pip install -r requirements.txt

📂 Estrutura de Arquivo
api-operadoras/
├── app.py               # Código principal da API
├── operadoras.csv       # Base de dados das operadoras (seu arquivo)
├── requirements.txt     # Dependências necessárias
└── README.md            # Esta documentação

⚙️ Configuração
Preparação do CSV:

Garanta que seu arquivo operadoras.csv tenha pelo menos estas colunas:
Registro_ANS,CNPJ,Razao_Social,Nome_Fantasia,Modalidade,UF

O separador deve ser ; (ponto-e-vírgula)

Variáveis de ambiente (opcional):
Crie um arquivo .env para configurações:
PORT=8000
CSV_PATH=operadoras.csv
CSV_SEPARATOR=;

🏃 Executando a API
python app.py

A API estará disponível em: http://localhost:8000

🌐 Endpoints Disponíveis
1. Health Check
Verifica o status da API e a carga de dados

GET /health
 Exemplo de resposta:
{
  "status": "OK",
  "rows_loaded": 2543,
  "columns": ["Registro_ANS", "CNPJ", ...]
}

2. Busca de Operadoras
Busca operadoras com filtros opcionais
GET /operadoras?termo=saude&uf=SP&limite=5

Parâmetros:

termo: Busca em Razao_Social, Nome_Fantasia ou CNPJ (opcional)

uf: Filtro por UF (opcional)

limite: Número máximo de resultados (padrão: 10)

Exemplo de resposta:
{
  "success": true,
  "count": 42,
  "results": [
    {
      "Registro_ANS": "12345",
      "CNPJ": "11.222.333/0001-44",
      "Razao_Social": "SAUDE EXEMPLO LTDA",
      "Nome_Fantasia": "PLANO SAUDE TOTAL",
      "UF": "SP"
    }
  ]
}

📚 Documentação Interativa
Acesse a documentação Swagger em:
http://localhost:8000/docs

