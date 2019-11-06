FROM ubuntu:latest
RUN apt-get update && apt-get -y install cron 
RUN apt-get -y install python3
RUN apt install -y python-pip
WORKDIR /githubexporter
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY github-cron /etc/cron.d/github-cron
COPY . /githubexporter

ENV ACCESS_TOKEN

RUN chmod 0644 /etc/cron.d/github-cron

# Apply cron job
RUN crontab /etc/cron.d/github-cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log
EXPOSE 8080
VOLUME /githubexporter
RUN python /githubexporter/main.py
CMD [ "python", "/githubexporter/githubcollector.py" ]
