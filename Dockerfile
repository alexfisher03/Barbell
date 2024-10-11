# Base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y nodejs npm \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    pkg-config \
    default-libmysqlclient-dev

# Set working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Install gunicorn for production use
RUN pip install gunicorn

# Create logging directory for DEBUG = False instances of the application
RUN mkdir -p /var/log/django

# Copy the entire application code to the Docker container
COPY . /app/

# Expose the port that your app runs on (8000 by default for Django)
EXPOSE 8000

# Define default command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
