from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

def setup_openai_llm():
    load_dotenv()

    assert os.getenv("OPENAI_API_KEY") is not None, ("OPENAI_API_KEY is not set. Please set it in .env file")

    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature=0.2,
        max_tokens=1000,
        verbose=True,
        timeout=None,
        api_key=os.getenv("OPENAI_API_KEY")
    )

    return llm