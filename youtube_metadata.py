import requests
from dotenv import load_dotenv
import os


def get_youtube_metadata(video_id):
    load_dotenv()
    rapidapi_key = os.getenv("RAPIDAPI_KEY")

    url = "https://youtube-metadata-extractor.p.rapidapi.com/get_youtube_video_title_description"

    querystring = {"url": f"https://youtu.be/{video_id}"}
    headers = {
        "x-rapidapi-key": f"{rapidapi_key}",
        "x-rapidapi-host": "youtube-metadata-extractor.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    video_name = data['data']['title']
    video_name = video_name[0:25]
    image_url = data['data']['thumbnails'][1]['url']

    print(video_name, image_url)
    return video_name, image_url
