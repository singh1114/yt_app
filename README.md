# yt_app

1. Export the secret key.
  ```
  export SECRET_KEY=something
  ```
2. Export the YouTube API Key.
  ```
  export YT_API_KEY=something
  ```
3. Install requirements
  ```
  pip install requirements.txt
  ```
4. Migrate DB changes (From the directory having manage.py)
  ```
  python manage.py migrate
  ```
5. APIs

Search API:
  - Default page size is 10
  ```
  curl --location --request GET 'http://127.0.0.1:8000/videos/search/Liverpool'
  ```

Detail API:
  - Default page size is 10
  ```
  curl --location --request GET 'http://127.0.0.1:8000/videos/details?page=1&limit=2'
  ```