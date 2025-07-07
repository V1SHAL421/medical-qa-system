import pytest
import requests

@pytest.fixture
def mock_response():
    yield {
        "status_code": 200,
        "response": {"data": []}
    }

def test_call_healthlake_api(mocker):
    mock_api_call = mocker.patch(requests.get, return_value=mock_response)