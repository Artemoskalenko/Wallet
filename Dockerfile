FROM python:3.10
RUN apt-get update -y
RUN apt-get upgrade -y

WORKDIR /app

COPY ./requirements.txt ./
RUN pip install -r requirements.txt
COPY . ./app

CMD ["python3.10", "./app/manage.py", "runserver", "0.0.0.0:8000"]