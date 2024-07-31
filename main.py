from langchain.llms import OpenAI

from dotenv import load_dotenv

load_dotenv()

llm = OpenAI()

result = llm("Write a very very short poem")

print(result)
