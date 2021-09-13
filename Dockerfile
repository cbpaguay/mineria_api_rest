FROM python:3.9.7-slim-buster
WORKDIR /opt/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD python ./api/app.py
