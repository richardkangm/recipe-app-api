FROM python:3.9-alpine
LABEL Richard Kang

ENV PYTHONUNBUFFERED 1

#install dependencies 
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# make dir, make it the working dir, and copy into docker image
RUN mkdir /app
WORKDIR /app
COPY ./app /app

# create a user for running applications only and switch user to user
# to be sure the application isnt run with root privileges
RUN adduser -D user
USER user
