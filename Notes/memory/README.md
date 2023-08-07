# Memory


LangChain provides a standard interface for memory and a collection of memory implementations.

Eg: we can easily store the message for the chatbot


```python
from langchain.memory import ChatMessageHistory

history = ChatMessageHistory()
history.add_user_message ("hi!")
```
