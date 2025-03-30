from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import os

app = FastAPI()

# Configuração CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Variável global para os dados
df = None

def load_data():
    global df
    try:
        csv_path = 'operadoras.csv'
        if not os.path.exists(csv_path):
            print("❌ Arquivo operadoras.csv não encontrado!")
            return False
        
        df = pd.read_csv(
            csv_path,
            sep=';',
            encoding='utf-8',
            dtype={'CNPJ': str, 'CEP': str, 'Telefone': str},
            on_bad_lines='warn'
        )
        print("✅ Dados carregados com sucesso!")
        print(f"Colunas disponíveis: {df.columns.tolist()}")
        return True
    except Exception as e:
        print(f"❌ Erro ao carregar CSV: {e}")
        return False

# Carrega os dados ao iniciar
load_data()

@app.get("/health", include_in_schema=True)
async def health_check():
    """Endpoint para verificação do status da API"""
    if df is None:
        return {"status": "ERROR", "message": "Dados não carregados"}
    
    return {
        "status": "OK",
        "rows_loaded": len(df),
        "columns": df.columns.tolist()
    }

@app.get("/operadoras", include_in_schema=True)
async def listar_operadoras(
    termo: str = Query(None, description="Termo para busca em Razao_Social, Nome_Fantasia ou CNPJ"),
    limite: int = Query(5, description="Número máximo de resultados", ge=1, le=100)
):
    if df is None:
        raise HTTPException(503, detail="Dados não disponíveis. Tente novamente mais tarde.")
    
    try:
        if termo:
            termo = str(termo).lower()
            mask = (
                df['Razao_Social'].str.lower().str.contains(termo, na=False) |
                df['Nome_Fantasia'].str.lower().str.contains(termo, na=False) |
                df['CNPJ'].str.contains(termo, na=False)
            )
            resultados = df[mask]
        else:
            resultados = df
        
        cols = ['Registro_ANS', 'CNPJ', 'Razao_Social', 'Nome_Fantasia', 'UF']
        return {
            "success": True,
            "count": len(resultados),
            "results": resultados[cols].head(limite).fillna('').to_dict('records')
        }
    except KeyError as e:
        raise HTTPException(400, detail=f"Coluna não encontrada: {str(e)}")
    except Exception as e:
        raise HTTPException(500, detail=f"Erro interno: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="debug"
    )