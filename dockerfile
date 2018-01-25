FROM python:latest

WORKDIR /usr/src/workrequest

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV OST=workrequest_pg
ENV ORD=b

RUN python manage.py migrate

EXPOSE 80

CMD ["gunicorn", "-b 0.0.0.0:80", "mysite.wsgi"]

