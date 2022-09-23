# Pull official base image
FROM python:3.10.7-alpine

# Set work directory
WORKDIR /webapp

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN apk add --no-cache git

RUN pip install --upgrade pip
COPY ./requirements*txt .

ARG OLD
RUN if [[ -z "$OLD" ]] ; then pip install -r requirements.txt ; else pip install -r requirements.old.txt ; fi

# Copy project
COPY . .

RUN python manage.py collectstatic --noinput
