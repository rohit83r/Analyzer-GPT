from autogen_ext.models.ollama import OllamaChatCompletionClient
import os
from dotenv import load_dotenv
load_dotenv()

def get_model_client():
# Assuming your Ollama server is running locally on port 11434.
    openai_model_client = OllamaChatCompletionClient(model="deepseek-r1:8b")


    return openai_model_client