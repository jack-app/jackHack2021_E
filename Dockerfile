FROM python:3.6

# install heroku cli
RUN curl https://cli-assets.heroku.com/install.sh | sh

RUN apt-get update && apt-get upgrade -y -qq
RUN apt-get install -y libgl1-mesa-dev
RUN pip install --upgrade pip

ENV DISPLAY=:99

WORKDIR /usr/src/app

ADD requirements.txt requirements.txt

RUN pip install -r requirements.txt

ADD . /usr/src/app