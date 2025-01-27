"""
Testes da aplicação (service de Google Planilhas, configuração do app e método GET principal)
"""
# pylint: disable=protected-access
# pylint: disable=redefined-outer-name
from unittest.mock import MagicMock
import pytest
from requests import Response
from gspread.exceptions import APIError
from app.service import count_values, get_structured_data
from app.config import get_settings
from app.main import retrieve_data

@pytest.fixture
def mocker():
    """
    Mock utilizado nos testes
    """
    return MagicMock()

def test_count_values():
    """
    Teste função de contagem de valores utilizada para contar respostas de determinada pergunta.
    """
    arr = [1, 2, 2, 3, 3, 3]
    expected_result = [{"value": 1, "count": 1}, {"value": 2, "count": 2}, {"value": 3, "count": 3}]
    assert count_values(arr) == expected_result

def test_count_values_empty_array():
    """
    Teste função de contagem de valores utilizada para contar respostas a partir de array vazio.
    """
    arr = []
    expected_result = []
    assert count_values(arr) == expected_result

def test_get_structured_data_success(mocker):
    """
    Cenário de sucesso do uso da biblioteca gspread e função que a utiliza
    """
    mocker.patch('gspread.service_account_from_dict')
    mocker.patch('gspread.Worksheet.get')
    get_structured_data()
    assert isinstance(get_structured_data(), dict)
    assert 'data' in get_structured_data()

def test_get_structured_data_api_error(mocker):
    """
    Cenário de sucesso do uso da biblioteca gspread e função que a utiliza
    """
    mock_response = Response()
    mock_response.status_code = 500
    mock_response._content = b'{"error": {"code": 500, "message": "Mocked API error"}}'
    mocker.patch('gspread.service_account_from_dict')
    mocker.patch('gspread.Worksheet.get', side_effect=APIError(mock_response))
    try:
        get_structured_data()
    except APIError as e:
        assert e.response.status_code == 500
        assert e.response._content == b'{"error": {"code": 500, "message": "Mocked API error"}}'

def test_get_settings():
    """
    Teste de obtenção e configuração das variáveis de ambiente
    """
    settings = get_settings()
    assert isinstance(settings, get_settings().__class__)
    assert settings.app_name == "PanoramADS API"
    assert settings.project_id is not None
    assert settings.private_key_id is not None
    assert settings.private_key is not None
    assert settings.client_email is not None
    assert settings.client_id is not None
    assert settings.client_url is not None

def test_get_success(mocker):
    """
    Cenário de sucesso da rota da aplicação
    """
    mock_response = {'data': 'Mocked API data'}

    mocker.patch('app.service.get_structured_data', return_value=mock_response)

    response = retrieve_data()

    assert 'data' in response

def test_get_error(mocker):
    """
    Cenário de sucesso da rota da aplicação
    """
    mock_error = APIError(Response())
    mocker.patch('app.service.get_structured_data', side_effect=mock_error)
    try:
        retrieve_data()
    except APIError as e:
        assert e.response.status_code == 500
        assert e.response._content == b'{"error": {"code": 500, "message": "Mocked API error"}}'
