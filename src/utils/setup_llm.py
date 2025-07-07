from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

def setup_openai_llm(expt_llm = "gpt-3.5-turbo", temperature=0.2):
    load_dotenv()

    assert os.getenv("OPENAI_API_KEY") is not None, ("OPENAI_API_KEY is not set. Please set it in .env file")

    llm = ChatOpenAI(
        model_name=expt_llm,
        temperature=temperature,
        max_tokens=1000,
        verbose=True,
        timeout=None,
        api_key=os.getenv("OPENAI_API_KEY")
    )

    return llm