# Base image
FROM python:3.10-slim

# Set environment vars
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set workdir
WORKDIR /code

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . .

# Expose port (for Django dev server)
EXPOSE 8000

# Default command (override in docker-compose)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
