from flask import Flask
from langchain.schema import (
   HumanMessage,
   SystemMessage
)
from langchain.chat_models import ChatOpenAI

app = Flask(__name__)

@app.route("/")
def index():
    return { "message": "Hello, world forever!!!" }
