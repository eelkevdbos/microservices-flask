FROM ubuntu:latest

MAINTAINER Eelke van den Bos "eelkevdbos@gmail.com"

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["concat.py"]