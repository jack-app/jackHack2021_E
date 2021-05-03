FROM python:3.6

# install heroku cli
RUN curl https://cli-assets.heroku.com/install.sh | sh

RUN apt-get update -qq
RUN pip install --upgrade pip
RUN apt-get install -y libgl1-mesa-dev

WORKDIR /usr/src/app

ADD requirements.txt requirements.txt

RUN pip install -r requirements.txt

ADD . /usr/src/app