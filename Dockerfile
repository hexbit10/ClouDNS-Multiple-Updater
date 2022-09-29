FROM python:3.7
WORKDIR /app
RUN apt-get update && apt-get -y install cron


COPY requirements.txt requirements.txt
COPY update.py update.py

RUN touch /var/log/cron.log

#Install python libraries
RUN pip3 install -r requirements.txt

# setup cron
COPY crontab /etc/cron.d/crontab
RUN chmod 0644 /etc/cron.d/crontab
CMD cron && tail -f /var/log/cron.log