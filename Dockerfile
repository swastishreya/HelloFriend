FROM python:3.7
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "./backend/manage.py", "runserver"]
