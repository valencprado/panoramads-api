# API PanoramADS

API simples que obtém dados de uma planilha proveniente de respostas de um formulário e formata para ser consumível ao Front-End.

## Tecnologias
- Python 3.13
- FastAPI
- gspread
- uvicorn
- python-dotenv

## Métodos

### GET
/: Obtém todos os valores enviados.
Formato de resposta:

```js
{
 question_name: [
{
  "value": "Yes",
  "count": 2
  },
{
  "value": "No",
  "count": 5
  }
]
}
```
