FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Don't copy the application code here
# It will be mounted as a volume for development
ENV PYTHONPATH=/app
EXPOSE 8001