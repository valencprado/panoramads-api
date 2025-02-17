"""
APIs da aplicação
"""
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from .service import get_structured_data

load_dotenv()

app = FastAPI()

origins = os.environ.get('ORIGINS').split(',')

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['GET'],
    allow_headers=['*']
)
@app.get("/")
def retrieve_data():
    """
    Método público que retorna dados formatados para gráficos
    """
    data = get_structured_data()
    return data
