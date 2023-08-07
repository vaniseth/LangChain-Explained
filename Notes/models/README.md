# MODELS

Models provides a generic interface for many LLMs, we can access models from OpenAI, Huggingface etc.

Models are basically LLM wrappers that allow us to connect large language models.

```python
from langchain.llms import OpenAI
from langchain import HuggingFaceHub
from langchain.llms import Cohere

llm = OpenAI(model_name = 'test-01')
llm = HuggingFaceHub(repo_id = 'google/flan-t5-xl')
llm = Cohere()

result = llm('Tell me a joke')
```
