from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
import cohere
from transformers import pipeline

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (for testing, restrict later)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)


# Cohere API setup
cohere_api_key = ""
co = cohere.Client(cohere_api_key)

# Emotion classifier
emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=1)

# Cat reactions
def get_cat_expression(emotion):
    cat_expressions = {
        "joy": "😺 (Happy Cat)",
        "sadness": "😿 (Sad Cat)",
        "anger": "😾 (Angry Cat)",
        "fear": "🙀 (Scared Cat)",
        "surprise": "😺😳 (Shocked Cat)",
        "neutral": "😼 (Normal Cat)"
    }
    return cat_expressions.get(emotion, "😼 (Default Cat)")

# Request Model
class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chatbot_response(request: ChatRequest):
    user_message = request.message

    # Detect emotion
    result = emotion_classifier(user_message)
    detected_emotion = result[0][0]['label']
    cat_expression = get_cat_expression(detected_emotion)

    # Generate AI response
    response = co.chat(
        message=user_message,
        model="command-r",
        temperature=0.7,
        preamble="You are Neko, a cute, friendly, and empathetic talking cat. Keep replies short and fun!"
    )

    chatbot_reply = response.text.strip()

    return {
        "reply": chatbot_reply,
        "emotion": detected_emotion,
        "cat_reaction": cat_expression
    }

