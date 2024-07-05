# Imports
import openai
import os
from fastapi import FastAPI, Form, Depends, Request
from utils import send_message
from dotenv import load_dotenv

load_dotenv()

# creating FastAPI application
app = FastAPI()

# Configuring OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

conversation_histories = {}


def conv_history(user_number, user_message, assistant_message):
    if user_number not in conversation_histories:
        conversation_histories[user_number] = []
    conversation_histories[user_number].append(
        {"role": "user", "content": user_message}
    )


@app.get("/")
async def root():
    return {"message": "Server is running"}


@app.post("/message")
async def reply(request: Request, Body=Form(), From=Form()):
    user_number = From.split(":")[1]
    user_message = Body
    print(f"Incoming message from {From}: {Body}")

    history = conversation_histories.get(user_number, [])
    history.append({"role": "user", "content": user_message})

    print(f"History before API call: {history}")

    openai_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=history
        + [{"role": "system", "content": "You are a helpful assistant."}],
        max_tokens=150,
    )

    reply_message = openai_response.choices[0].message.content

    print(f"Assistant's response: {reply_message}")

    conv_history(user_number, user_message, reply_message)
    print(f"History after updating: {conversation_histories}")

    send_message(user_number=user_number, message=reply_message)
