FROM python:3.7.7
ARG RUNTIME_DEPS='wget axel vim python-dev libsm6 libxext6'
RUN apt-get update -y && \
    apt-get install -y ${RUNTIME_DEPS}

# Added separately so that layers get cached
ARG BUILD_DEPS='apt-utils unzip cmake build-essential pkg-config  build-essential'

COPY yt_app/requirements.txt .
RUN apt-get install -y ${BUILD_DEPS} && \
    pip install -r requirements.txt && \
    apt-get purge -y --auto-remove $BUILD_DEPS

# set workdir
WORKDIR /var/app

# copy code into image
COPY . /var/app/

EXPOSE 8000

# entrypoint
ENTRYPOINT ["python"]
CMD ["yt_app/manage.py", "migrate"]
CMD ["yt_app/manage.py", "runserver", "0.0.0.0:8000"]