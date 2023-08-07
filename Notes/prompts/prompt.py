from langchain import PromptTemplate
import dotenv

from dotenv import load_dotenv
load_dotenv()

template = """Question: {question}
How to make tea?
Answer : """

prompt = PromptTemplate(template = template, input_variables = ['question'])

user_input = input('Ask your question here?')
prompt.format(question = user_input)