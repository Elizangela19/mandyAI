from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from model.model_utils import load_model, get_best_response

# Initialize FastAPI app
app = FastAPI()

# Load the model once when the app starts
model = load_model()

# Define request format
class UserQuery(BaseModel):
    query: str

# Predefined responses (you can expand these)
responses = [
    "Hi! How can I help you today?",
    "Investing is a great way to grow your savings.",
    "Budgeting is key to successful financial planning.",
    "Consider tracking your expenses using an app."
]

# API endpoint to handle user queries
@app.post("/chat")
def chat_endpoint(user_query: UserQuery):
    try:
        best_response = get_best_response(model, user_query.query, responses)
        return {"response": best_response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
