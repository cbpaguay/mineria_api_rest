FROM python:3.9.7-slim-buster
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY /app/* ./
EXPOSE 8017
CMD [ "python", "./app.py" ]