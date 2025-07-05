from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

def setup_openai_llm():
    load_dotenv()
    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature=0.2,
        max_tokens=1000,
        verbose=True,
        timeout=None,
        api_key=os.getenv("OPENAI_API_KEY")
    )
    print("The LLM has been created")
    return llm