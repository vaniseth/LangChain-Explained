# Agents and Tools

This is an extremely powerful module, we can setup agents that can use tools like google search and Wikipedia or calculator.

Agents allow the LLM to interact with external APIs

```python
from langchain.agents import load_tools
from langchain.agents import initialize_agent

from langchain.llms import OpenAI

llm = OpenAI( temperature = 0.9 )

tools = load_tools( ['google-search', 'Wikipedia', 'llm-math'],
llm = llm )
agent = initialize_agent( tools, llm, agent = 'zero-shot-react-description')

agent.run ('Who was the lead actor in Interstellar? What is his current age raised to the power of 0.21?')
```


### Working

