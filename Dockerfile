FROM python:3.7
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
RUN pytest
EXPOSE 8000
CMD ["python", "-m", "manage.py", "runserver"]
