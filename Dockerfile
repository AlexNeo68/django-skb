from python:3.11.5

ENV PYTHONUNUNBUFFERED=1

WORKDIR /app

RUN pip install "poetry==1.7.1"

RUN poetry config virtualenvs.create false --local

COPY pyproject.toml poetry.lock ./

RUN poetry install

COPY mysite .

CMD ["gunicorn", "mysite.wsgi:application", "--bind", "0.0.0.0:8000"]