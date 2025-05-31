# Sistema de Gestión de Sílabos Universitarios

Este sistema permite gestionar los sílabos académicos de una universidad, proporcionando funcionalidades CRUD completas y una API REST.

## Requisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Instalación

1. Crear un entorno virtual:
```bash
python -m venv venv
```

2. Activar el entorno virtual:
- Windows:
```bash
.\venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Realizar las migraciones:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Crear un superusuario:
```bash
python manage.py createsuperuser
```

6. Ejecutar el servidor:
```bash
python manage.py runserver
```

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:
- `silabos/`: Aplicación principal para la gestión de sílabos
- `universidad/`: Configuración principal del proyecto Django
- `api/`: Endpoints de la API REST

## Características
- CRUD completo para sílabos
- API REST
- Interfaz administrativa de Django
- Filtros y búsqueda avanzada
- Autenticación y autorización 