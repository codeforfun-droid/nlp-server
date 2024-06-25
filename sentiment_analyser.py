import joblib
import requests
from dotenv import load_dotenv
import os

def get_comments(videoId):
    cursor_token = ""
    comments = []
    load_dotenv()
    rapidapi_key = os.getenv("RAPIDAPI_KEY")

    for i in range(0, 1):
        url = "https://youtube138.p.rapidapi.com/video/comments/"

        if cursor_token == "":
            querystring = {"id": videoId, "hl": "en", "gl": "US"}
        else:
            querystring = {"id": videoId, "cursor": cursor_token, "hl": "en", "gl": "US"}

        headers = {
            "x-rapidapi-key": f"{rapidapi_key}",
            "x-rapidapi-host": "youtube138.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()
        cursor_token = data['cursorNext']
        for comment_data in data['comments']:
            comments.append(comment_data['content'])

    return comments


def predict_scores(comments):
    positive = 0
    neutral = 0
    negative = 0

    model = joblib.load('sentiment_analysis_svm_model.pkl')
    vectorizer = joblib.load('vectorizer.pkl')

    print("Process Initiated....")

    for comment in comments:
        X = vectorizer.transform([comment])
        y_pred = model.predict(X)[0]
        if y_pred == 1:
            positive += 1
        elif y_pred == 0:
            neutral += 1
        else:
            negative += 1

    positive = (positive / len(comments)) * 100
    negative = (negative / len(comments)) * 100
    neutral = (neutral / len(comments)) * 100

    print(f"positive:{positive}, negative:{negative}, neutral:{neutral}")
    print("Process Completed..")
    return positive, negative, neutral

def get_sentiment(videoId):
    comments = get_comments(videoId)
    positive, negative, neutral = predict_scores(comments)
    return positive, negative, neutral







