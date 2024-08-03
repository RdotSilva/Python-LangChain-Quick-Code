from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import argparse

from dotenv import load_dotenv

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument("--task", default="return a list of numbers")
parser.add_argument("--language", default="python")
args = parser.parse_args()

llm = OpenAI()


code_prompt = PromptTemplate(
    template="Write a very short {language} function that will {task}",
    input_variables=["language", "task"],
)
test_prompt = PromptTemplate(
    template="Write test for the following {language} code:\n{code}",
    input_variables=["language", "code"],
)

code_chain = LLMChain(llm=llm, prompt=code_prompt, output_key="code")

result = code_chain({"language": args.language, "task": args.task})

print(result["text"])
