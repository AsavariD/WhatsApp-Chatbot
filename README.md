# WhatsApp Bot using Twilio and OpenAI

**Installation Libraries**: `python`, `twilio`, `openai`, `pyngrok`, `uvicorn`, `fastapi`, `python-decouple`, `python-multipart`

### Steps:

**Step 1**: Create a Twilio account and set up the WhatsApp Sandbox. Note down your Twilio account SID, Auth token, and sandbox number.

**Step 2**: Create an OpenAI account and generate an API key.

**Step 3**: Create a Python virtual environment and install the required libraries.

**Step 4**: Create a `utils.py` file to handle interactions with the Twilio API for sending WhatsApp messages.

#### Key Components of `utils.py`:
- **Imports**:
  - `twilio.rest.Client`: The Twilio client library for making API calls.
  - `decouple import config`: A utility for managing configuration through environment variables.
- **Twilio Authentication**:
  - Retrieve the Twilio account SID and Auth token from environment variables.
  - Authenticate and create a `Client` object for Twilio API interaction.
- **Phone Numbers**:
  - Retrieve the Twilio phone number from an environment variable.
- **`send_message` Function**:
  - **Parameters**: `user_number` (the recipient's phone number) and `message` (the content of the message).
  - **Functionality**: Use the Twilio client to send a WhatsApp message. Construct the message with the recipient's number and message content, then send it using the Twilio API.

**Step 5**: Create a `main.py` file to handle incoming HTTP requests, interact with the OpenAI API for generating responses, and utilize the Twilio API to send WhatsApp messages.

#### Key Components of `main.py`:
- **Imports**:
  - `fastapi`: To create the web application and handle HTTP requests.
  - `openai`: To interact with the OpenAI API for generating responses.
  - `decouple import config`: To manage configuration through environment variables.
  - `Request` and `Form`: To handle incoming form data in requests.
  - `send_message` from `utils`: To send WhatsApp messages via Twilio.
- **Application Setup**:
  - Instantiate the FastAPI application.
  - Configure the OpenAI API key using environment variables.
  - Retrieve the user's WhatsApp number from environment variables.
- **Endpoints**:
  - **GET /**: A simple check endpoint that returns a message indicating the server is running.
  - **POST /message**: An endpoint to handle incoming messages, generate a response using OpenAI's GPT-3.5-turbo model, and send the response back to the user via Twilio.

**Step 6**: Start the FastAPI application with the command:
```sh
uvicorn main:app --reload
```

**Step 7**: Host the application on a public server using `ngrok`. Authenticate `ngrok` with your auth token:
```sh
ngrok config add-authtoken $YOUR_AUTHTOKEN
```

**Step 8**: While the FastAPI application is running, run this `ngrok` command:
```sh
ngrok http 8000
```
This command establishes a connection between your local server on port 8000 and a public URL provided by the ngrok.io service.

**Step 9**: Go to the Twilio Console and select the Messaging tab from the left panel. Under the Try it out section, click on Send a WhatsApp message. Navigate to the Sandbox settings tab. Copy the ngrok.io forwarding URL, append `/message` to it, and paste it into the box labeled “WHEN A MESSAGE COMES IN”.

**Step 10**: Send a message from your WhatsApp number and test the chatbot.

---
