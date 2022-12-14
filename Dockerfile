FROM python:3.9.15-alpine3.16
COPY requirements.txt requirements.txt
COPY app.py app.py
COPY ./app /app
COPY config.py config.py
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python","app.py"]
