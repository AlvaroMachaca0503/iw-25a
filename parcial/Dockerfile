FROM python:3.11-slim

WORKDIR /app

# Instala pg_isready y librerías para psycopg2 (si usas psycopg2-binary no necesitas libpq-dev)
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      postgresql-client \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
