# TODO-List-App
Django / Python3.6 TODO List Application

This is a simple CRUD application for a browser-based TODO list. You can track your upcoming activities as
well as their subjects and due dates. Deployment is handled via docker and docker-compose.

## Deployment Steps
1. Clone this repository onto your machine

`git clone https://github.com/gsblinkhorn/TODO-List-App.git`

2. Add your domain to ALLOWED_HOSTS (you can skip this if you are running locally)

`vim TRACKER/settings.py`

Change ALLOWED_HOSTS = ['0.0.0.0','127.0.0.1','localhost',] to ALLOWED_HOSTS = ['0.0.0.0','127.0.0.1','localhost', $YOUR_HOST_HERE]

3. Run `docker-compose up` from the project's root directory

After building the image and starting the docker container, the TODO app should be available on your domain at port 8000
