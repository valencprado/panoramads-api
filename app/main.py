"""
APIs da aplicação
"""
from fastapi import FastAPI
from dotenv import load_dotenv
from .service import get_structured_data

load_dotenv()

app = FastAPI()


@app.get("/")
def retrieve_data():
    """
    Método público que retorna dados formatados para gráficos
    """
    data = get_structured_data()
    return data
