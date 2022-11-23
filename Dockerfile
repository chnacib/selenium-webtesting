FROM python:3.9

COPY . .
RUN pip install poetry
RUN poetry install 
CMD poetry run pytest ./tests/main.py