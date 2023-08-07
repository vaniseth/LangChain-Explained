# PROMPTS

This includes prompt management, prompt optimization, and serialization.

Prompt templates allows us to avoid having to hard code text which is input to the LLMs

Here we can define prompt templates that take user input and create the final prompt for the model.

```python
from langchain import PromptTemplate

template = """Question: {question}
How to make tea?
Answer : """

prompt = PromptTemplate(template = template, input_variables = ['question'])

user_input = input('Ask your question here?')
prompt.format(question = user_input)
```
