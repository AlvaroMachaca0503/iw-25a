# API REST Universidad

Este proyecto implementa una API REST para gestionar sílabos universitarios con autenticación JWT.

## Requisitos

- Python 3.8+
- pip (gestor de paquetes de Python)
- Entorno virtual (recomendado)

## Configuración del Proyecto

1. Clonar el repositorio:
```bash
git clone <url-del-repositorio>
cd django-rest
```

2. Crear y activar el entorno virtual:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Crear archivo .env en la raíz del proyecto:
```env
SECRET_KEY=tu-clave-secreta-aqui
DEBUG=True
```

5. Realizar migraciones:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Crear superusuario:
```bash
python manage.py createsuperuser
```

7. Ejecutar el servidor:
```bash
python manage.py runserver
```

## Uso de la API

### Autenticación con JWT

1. Obtener token (POST):
```bash
curl -X POST http://localhost:8000/api/token/ -H "Content-Type: application/json" -d '{"username": "tu_usuario", "password": "tu_contraseña"}'
```
Respuesta:
```json
{
    "access": "token-de-acceso",
    "refresh": "token-de-refresco"
}
```

2. Refrescar token (POST):
```bash
curl -X POST http://localhost:8000/api/token/refresh/ -H "Content-Type: application/json" -d '{"refresh": "tu-token-de-refresco"}'
```

3. Verificar token (POST):
```bash
curl -X POST http://localhost:8000/api/token/verify/ -H "Content-Type: application/json" -d '{"token": "tu-token-de-acceso"}'
```

### Endpoints sin Token (GET)

Los siguientes endpoints están disponibles sin autenticación:

```bash
# Listar sílabos (GET)
curl http://localhost:8000/api/silabos/

# Ver detalle de un sílabo (GET)
curl http://localhost:8000/api/silabos/{id}/
```

### Endpoints con Token (POST/PUT/DELETE)

Para estos endpoints, necesitas incluir el token en el header:

```bash
# Crear nuevo sílabo (POST)
curl -X POST http://localhost:8000/api/silabos/ \
  -H "Authorization: Bearer tu-token-de-acceso" \
  -H "Content-Type: application/json" \
  -d '{"campo1": "valor1", "campo2": "valor2"}'

# Actualizar sílabo (PUT)
curl -X PUT http://localhost:8000/api/silabos/{id}/ \
  -H "Authorization: Bearer tu-token-de-acceso" \
  -H "Content-Type: application/json" \
  -d '{"campo1": "nuevo_valor1"}'

# Eliminar sílabo (DELETE)
curl -X DELETE http://localhost:8000/api/silabos/{id}/ \
  -H "Authorization: Bearer tu-token-de-acceso"
```

## Optimizaciones Implementadas

1. **Autenticación JWT**: Implementación segura de tokens JWT con rotación de refresh tokens.
2. **Rate Limiting**: Límites de tasa para prevenir abuso de la API.
3. **Caché**: Configuración de caché para mejorar el rendimiento.
4. **CORS**: Configuración de CORS para permitir peticiones desde otros dominios.
5. **Paginación**: Implementación de paginación para grandes conjuntos de datos.
6. **Filtros**: Soporte para filtrado de datos mediante django-filter.

## Seguridad

- Las variables sensibles están configuradas a través de variables de entorno.
- Los tokens JWT tienen una duración limitada.
- Se implementa rate limiting para prevenir ataques de fuerza bruta.
- CORS está configurado para mayor seguridad.

## Notas Importantes

- En producción, asegúrate de configurar `DEBUG=False`
- Configura `ALLOWED_HOSTS` y `CORS_ALLOW_ALL_ORIGINS` apropiadamente
- Utiliza HTTPS en producción
- Mantén las dependencias actualizadas 