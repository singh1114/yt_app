# yt_app

1. Build docker file
```
docker build -t videos .
```

2. Run docker
```
docker run --env SECRET_KEY=something --env YT_API_KEY=AIzaSyDGTi-XXXXXzX0DEv4 -p 8000:8000 -it videos
```

3. APIs

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