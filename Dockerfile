from python:3.10.1

ENV PYTHONUNUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -upgrade pip
RUN pip install -r requirements.txt

COPY mysite .

CMD ["gunicorn", "mysite.wsgi:application", "--bind", "0.0.0.0:8000"]