from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
import os

# 1. Initialize the Server
app = FastAPI()

# 2. Securely grab the API key from the server's hidden environment
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# 3. Define the shape of incoming data
class UserInput(BaseModel):
    message: str

# 4. Create the core thinking endpoint
@app.post("/think")
def think(user_input: UserInput):
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=user_input.message
    )
    return {"ikigai_says": response.text}

# 5. A simple heartbeat to check if the server is alive
@app.get("/")
def health_check():
    return {"status": "Ikigai Core Server is Online."}
