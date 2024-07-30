from langchain.llms import OpenAI

from dotenv import load_dotenv

load_dotenv()

result = llm("Write a very very short poem")

print(result)