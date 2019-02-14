# TODO Activity Tracker Site
# Version: 1.0
# Reference: https://semaphoreci.com/community/tutorials/dockerizing-a-python-django-web-application

FROM python:3.6

# Clean container
RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean

# Project Files and Settings
ARG PROJECT=TRACKER
ARG PROJECT_DIR=/var/www/${PROJECT}
RUN mkdir -p $PROJECT_DIR
WORKDIR $PROJECT_DIR
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Server
EXPOSE 8000
STOPSIGNAL SIGINT

COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["django"]