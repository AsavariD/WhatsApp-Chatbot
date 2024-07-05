# imports
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

# to authenticate twilio account
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)  # client object to interact with Twilio API

# phone numbers
twilio_number = os.getenv("TWILIO_NUMBER")


# Function to send message from twilio to user
def send_message(user_number, message):
    client.messages.create(
        from_="whatsapp:" + twilio_number, body=message, to="whatsapp:" + user_number
    )
