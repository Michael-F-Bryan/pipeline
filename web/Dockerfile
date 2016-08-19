FROM python:3.5

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

# Sort out dependencies
COPY ./requirements.txt .
RUN pip install -r ./requirements.txt

COPY . /usr/src/app

# CMD [ '/usr/local/bin/gunicorn' 'app.wsgi:application' '-w' '2' '-b' '0.0.0.0:8000']
