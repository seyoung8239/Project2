FROM python:3.9.7

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 8000