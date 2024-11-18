#pull official base image
#docker ayaklandigi zaman o arkada linux kaldirip icinde calistiracak
FROM python:3.10-slim
# Kurulan Linux güncellenir ve geliştirme araçları yüklenir
RUN apt-get update && apt-get install -y \
    python3-dev \
    build-essential \
    --no-install-recommends && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

#set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV VIRTUAL_ENV = /opt/venv
#pip requirements
RUN pip install --upgrade pip
RUN pip install virtualenv && python -m virtualenv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

ADD ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
#burdaki tek tek islenen islemleri loglardan takip icin bizim runserver kurmamiz gerek
#runserver kosabilmek icin de linux iicnde tüm dosyaların olması gerekmektedir
#hersey linux a gitti
COPY .  /srv/app
#bundan sonraki komuların srv dizininde koşmasını istediğimiz icin workdir kullanıldı
WORKDIR /srv/app
