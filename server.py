from fastapi import FastAPI
from chat_new import create_chatbot
from langserve import add_routes
from dotenv import load_dotenv
load_dotenv()

chatbot = create_chatbot()

app = FastAPI(
  title="LangChain Server",
  version="1.0",
  description="A simple api server using Langchain's Runnable interfaces",
)

add_routes(
    app,
    chatbot,
    path="/openai",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
