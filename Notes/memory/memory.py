from langchain.memory import ChatMessageHistory
import dotenv

from dotenv import load_dotenv
load_dotenv()

history = ChatMessageHistory()
history.add_user_message ("hi!")