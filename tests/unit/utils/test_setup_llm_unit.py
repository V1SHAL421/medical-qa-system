import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../..'))
from src.utils.setup_llm import setup_openai_llm
import pytest

@pytest.mark.unit
def test_setup_llm_succeeds(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "valid_key")
    test_llm = setup_openai_llm()
    assert test_llm.model_name == "gpt-3.5-turbo"