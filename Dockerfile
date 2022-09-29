FROM python:3.9
WORKDIR /app
RUN apt-get update && apt-get -y install cron


COPY requirements.txt requirements.txt
COPY update.py update.py

RUN touch /var/log/cron.log

#Install python libraries
RUN python3 -m pip install -r requirements.txt

# setup cron
COPY crontab /etc/cron.d/crontab
RUN chmod 0644 /etc/cron.d/crontab
RUN crontab /etc/cron.d/crontab
CMD ["cron","-f", "-L", "2"]