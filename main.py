from typing import Union
import uvicorn
import sentiment_analyser as sa
import youtube_metadata as ym
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

app = FastAPI()

# CORS (Cross-Origin Resource Sharing) middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (modify as needed)
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Add more HTTP methods as needed
    allow_headers=["*"],  # Allow all headers (modify as needed)
)


@app.get("/")
def read_root():
    positive, negative, neutral = 0, 0, 0
    return {"positive": positive, "negative": negative, "neutral": neutral}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/api/v1/get_sentiment/{video_id}")
def read_item(video_id: str):
    positive, negative, neutral = sa.get_sentiment(video_id)
    return {
        "positive": positive,
        "negative": negative,
        "neutral": neutral
    }


@app.get("/api/v1/get_metadata/{video_id}")
def read_item(video_id: str):
    video_name, image_url = ym.get_youtube_metadata(video_id)
    return {
        "video name": video_name,
        "image_url": image_url
    }


@app.get("/api/v1/get_data/{video_id}")
def read_item(video_id: str):
    video_name, image_url = ym.get_youtube_metadata(video_id)
    positive, negative, neutral = sa.get_sentiment(video_id)
    return {
        "meta-data": {
            "video name": video_name,
            "image_url": image_url
        }, "sentiments": {
            "positive": positive,
            "negative": negative,
            "neutral": neutral
        }
    }


# app/main.py
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

