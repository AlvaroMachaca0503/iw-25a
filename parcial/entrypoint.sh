#!/usr/bin/env bash
set -e

# 1) Esperar a que la base de datos esté lista
until pg_isready -h "${DB_HOST:-db}" -p "${DB_PORT:-5432}" > /dev/null 2>&1; do
  echo "Esperando a la base de datos en ${DB_HOST:-db}:${DB_PORT:-5432}..."
  sleep 1
done

# 2) Aplicar migraciones
echo "Aplicando migraciones..."
flask db upgrade

# 3) Sembrar datos si la tabla 'courses' está vacía
if [ -z "$(psql "$DATABASE_URL" -tAc "SELECT 1 FROM courses LIMIT 1")" ]; then
  echo "Tabla 'courses' vacía. Ejecutando seeder..."
  flask seed
else
  echo "Datos ya existen. Omitiendo seeder."
fi

# 4) Arrancar Flask
echo "Iniciando servidor Flask..."
exec flask run --host=0.0.0.0
