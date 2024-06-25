# YouTube Sentiment Analysis API

This FastAPI application provides endpoints to fetch YouTube video metadata and perform sentiment analysis on comments using a pretrained NLP model.

## Setup

1. **Clone the Repository:**
    ```
   git clone https://github.com/KumarUtsav1025/sentiment_analysis_server
   cd sentiment_analysis_server
    ```

2. **Install Dependencies:**
     ```
     pip install requirements.txt
     ```

3. **Run the Application:**
      ```
      uvicorn main:app --reload
      ```
   - The API server will start at `http://127.0.0.1:8000`.

## Endpoints

### Fetch Video Metadata

**Endpoint:** `/api/v1/get_metadata/{video_id}`

- **Description:** Retrieves metadata such as video name and image URL for a given YouTube video ID.

- **Example:**
GET http://127.0.0.1:8000/api/v1/get_metadata/<video_id>


### Analyze Sentiment of Video Comments

**Endpoint:** `/api/v1/get_sentiment/{video_id}`

- **Description:** Analyzes sentiment (positive, negative, neutral) of comments related to a YouTube video using a pretrained NLP model.

- **Example:**
GET http://127.0.0.1:8000/api/v1/get_sentiment/<video_id>


### Combined Data Endpoint

**Endpoint:** `/api/v1/get_data/{video_id}`

- **Description:** Retrieves both video metadata and sentiment analysis results in a combined response.

- **Example:**
GET http://127.0.0.1:8000/api/v1/get_data/<video_id>



## CORS Configuration

- The application is configured to allow cross-origin resource sharing (CORS) from all origins (`*`). CORS middleware is enabled to handle requests from different domains.

## Usage

- Replace `<video_id>` with a valid YouTube video ID to fetch corresponding data and sentiment analysis.
- The sentiment analysis is performed using a custom NLP model trained on comments associated with the specified video.

## Notes

- Ensure all API requests are properly authenticated and authorized if deployed in a production environment.
- Modify CORS settings (`allow_origins`, `allow_methods`, `allow_headers`) in `main.py` as per your application.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.
