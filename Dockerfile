FROM python:3.9-slim

WORKDIR /app

COPY requirements_simple.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app_simple.py app.py

EXPOSE 5000

CMD ["python", "app.py"]
