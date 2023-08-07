# Indexes

This module uses many utility functions to combine your model with your own text data.

Indexes allows us to extract relevant information for the LLMs

Eg: It provides the document loaders to load the data from different sources like notions, csv, or emails. Basically, any piece of text and associated metadata

```python
from langchain.document_loaders.notion import NotionDirectortLoader
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.document_loaders import PyPDFLoader
from langchain.document_lloaders.email import UnStructuredEmailLoader

loader = NotionDirectoryLoader('Notion_DB')
loader = CSVLoader ('testing.csv')
loader = PyPDFLoader ('testing.pdf')
loader = UnStructuredEmailLoader('testing-email.eml')

data = loader.load()
```

It also provides vector store interfaces to efficiently store the text and make it searchable

```python
from langchain.vectorstores import Pinecone
from langchain.vectorstores iport Weaviate
from langchain.vectorstores import FAISS
from langchain.vectorstores import ElasticVectorSearch
from langchain.vectorstores import OpenSearchVectorSearch
from langchain.vectorstores.redis import Redis
from langchain.vectorstores import AtlasDB
from langchain.vectorstores import Milvus

db = FAISS.from documents(docs, embeddings)

docs = db.similarity_search(query)
```
