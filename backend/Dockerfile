# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY wait-for-it.sh /usr/wait-for-it.sh

# Set work directory
WORKDIR /code/src

RUN chmod +x /usr/wait-for-it.sh

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libmariadb-dev \
    libmariadb-dev-compat \
    pkg-config \
    # Dependencies for WeasyPrint
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libgdk-pixbuf2.0-0 \
    libcairo2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY ./requirements.txt /code/src/
RUN pip install --upgrade pip && pip install -r requirements.txt


# Copy project
COPY ./src /code/src

CMD /usr/wait-for-it.sh -t 60 db:3306 -- python manage.py migrate && python manage.py collectstatic --noinput && gunicorn itskompetent.wsgi:application --bind 0.0.0.0:8000 --workers 3 --threads 2
# Expose the port the app runs on
EXPOSE 8000



