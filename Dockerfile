FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /app

ADD . /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install cmake
COPY . /app
RUN pip install -r requirements.txt

COPY . /app
RUN apt-get update ##[edited]
RUN apt-get install 'ffmpeg'\
    'libsm6'\ 
    'libxext6'  -y
