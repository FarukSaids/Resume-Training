#pull official base image
#docker ayaklandigi zaman o arkada linux kaldirip icinde calistiracak
FROM python:3.10-slim
#kurulan linux guncellenir
RUN apt-get update
RUN apt-get install python3-dev build-essential -y #gelistirici kitlerdir kütüphane

#pip requirements
RUN pip install --upgrade pip
RUN pip install virtualenv && python -m virtualenv /opt/venv

ADD ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
#burdaki tek tek islenen islemleri loglardan takip icin bizim runserver kurmamiz gerek
#runserver kosabilmek icin de linux iicnde tüm dosyaların olması gerekmektedir
#hersey linux a gitti
COPY .  /srv/app
#bundan sonraki komuların srv dizininde koşmasını istediğimiz icin workdir kullanıldı
WORKDIR /srv/app
RUN python manage.py runserver