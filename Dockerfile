FROM python:alpine

LABEL maintainer="Adam Dodman <hello@adam-ant.co.uk>" \
      org.label-schema.vendor="Adam-Ant" \
      org.label-schema.name="TelegramVideoBot" \
      org.label-schema.url="https://github.com/Adam-Ant/tg-random-video-bot" \
      org.label-schema.description="Telegram bot for serving random videos from a pool" \
      org.label-schema.version="0.1"

COPY requirements.txt main.py /

RUN pip3 install -r /requirements.txt

VOLUME /world

ENTRYPOINT ["python3", "-u", "/main.py"]
