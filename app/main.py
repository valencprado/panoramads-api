from fastapi import FastAPI
from .service import get_structured_data
# from dotenv import load_dotenv

# load_dotenv()

app = FastAPI()


@app.get("/")
def retrieve_data():
  data = get_structured_data()
  return data
