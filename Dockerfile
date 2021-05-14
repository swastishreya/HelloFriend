FROM python:3.7
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN python ./backend/manage.py migrate
COPY . .
EXPOSE 8000
CMD ["python", "./backend/manage.py", "runserver"]
