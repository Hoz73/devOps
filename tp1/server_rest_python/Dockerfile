# syntax=docker/dockerfile:1

FROM python:3.9-slim-buster as build
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python", "app.py"]

#docker run -it --rm hoz73/server_python_docker
#docker run -it --rm hoz73/client_python_docker

