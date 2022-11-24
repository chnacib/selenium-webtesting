FROM python:3.9

COPY ./tests .
RUN pip install poetry
RUN poetry install 
CMD poetry run pytest -s main.py