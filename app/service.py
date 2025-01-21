"""
Módulo responsável pela manipulação e captura de dados do formulário
por meio do Google Planilhas.
"""
import os
import gspread

credentials = {
  "type": "service_account",
  "project_id": os.getenv("PROJECT_ID"),
  "private_key_id": os.getenv("PRIVATE_KEY_ID"),
  "private_key": os.getenv("PRIVATE_KEY"),
  "client_email": os.getenv("CLIENT_EMAIL"),
  "client_id": os.getenv("CLIENT_ID"),
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": os.getenv("CLIENT_URL"),
  "universe_domain": "googleapis.com"
}

def count_values(arr):
    """
    Função contadora de respostas dadas
    """
    return [{"value": value, "count": arr.count(value)} for value in set(arr)]

def get_structured_data():
    """
    Método que formata os dados
    """
    try:
        gc = gspread.service_account_from_dict(credentials)
        sh = gc.open_by_key("1QKW0sD2zePl-lNdxQfWzeNgxsY_PUHUSOsjkAMB1AhI")
        ws = sh.sheet1
        data = ws.get("B2:M", major_dimension="COLUMNS")
        perguntas = ["idade", "genero", "semestre", "atuacao_atual", "modalidade_trabalho", "regiao_trabalho", "regiao", 
                     "porte_empresa", "area_atual", "area_desejo", "satisfacao_trabalho", "dificuldade_trabalho"]

        data_formatted = {
          name: count_values(data[i]) for i, name in enumerate(perguntas)
        }
        
        return {"data": data_formatted}
    except gspread.exceptions.APIError as exception:
        return {"code": 500, "message": "Internal Server Error", "details": f"{exception}"}