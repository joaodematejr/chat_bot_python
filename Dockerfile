FROM python:3.8

RUN pip install --upgrade pip

RUN pip install --upgrade setuptools

RUN pip install --upgrade chatterbot

RUN pip install --upgrade chatterbot-corpus

COPY main.py /

CMD [ "python", "./main.py" ]