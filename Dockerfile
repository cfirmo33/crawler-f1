FROM python:3.6.2
RUN apt-get update && apt-get install -y python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
ADD requirements.txt /usr/src/app/requirements.txt
ADD crawler-f1.sh /usr/src/app/crawler-f1.sh
WORKDIR /usr/src/app
RUN pip install -r requirements.txt
RUN ["chmod", "+x", "crawler-f1.sh"]
