from pydantic import BaseModel

class Operadora(BaseModel):
    registro_ans: str
    cnpj: str
    razao_social: str
    # Adicione todos os campos do seu CSV aqui