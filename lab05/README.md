# ⚙️ Laboratorio 5 - Framework Web con Django

## 📚 Introducción  
Este laboratorio tiene como objetivo la implementación básica de un **framework web** utilizando el lenguaje **Python** junto con el entorno **Django**, ejecutado sobre un sistema **Ubuntu**.

## 🧰 Requisitos Previos

- Python 3 instalado en tu sistema  
- Vim u otro editor de texto (opcional)  
- Ubuntu 20.04 o una versión más reciente  
- Conexión activa a Internet  

## 🖥️ Preparación del Entorno

Sigue los pasos a continuación para configurar el entorno virtual y ejecutar un proyecto en Django:

### 1️⃣ Clonar este repositorio

Ejecuta en tu terminal:

```bash
git clone https://github.com/AlvaroMachaca0503/iw-25a.git
```

### 2️⃣ Acceder a la carpeta del repositorio

```bash
cd iw-25a
```

### 3️⃣ Entrar a la carpeta del laboratorio 5

```bash
cd lab05
```

### 4️⃣ Crear un entorno virtual

```bash
mkdir env
cd env
virtualenv -p python3 .
```

### 5️⃣ Activar el entorno virtual

Desde la misma carpeta, ejecuta:

```bash
source ./../env/bin/activate
```

### 6️⃣ Instalar Django dentro del entorno

```bash
pip install Django
```

### 7️⃣ Acceder a la carpeta del proyecto Django

```bash
cd ..
cd MyDjangoProject
```

### 8️⃣ Crear un superusuario para acceder al panel administrativo

```bash
python manage.py createsuperuser
```

Completa los datos solicitados:

- Nombre de usuario  
- Correo electrónico  
- Contraseña (escríbela dos veces)  

Confirma con `y` si te lo solicita.

### 9️⃣ Ejecutar migraciones y levantar el servidor local

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### 🔟 Acceder al panel administrativo

Abre tu navegador y visita:

🔗 [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

Inicia sesión con los datos del superusuario que creaste.

---

## ✅ Conclusión

Al seguir estos pasos, habrás desplegado un entorno Django funcional y accederás al panel administrativo desde tu navegador. Este laboratorio representa una base sólida para futuros desarrollos web más complejos en Python usando Django.

---

**Autor:**  
[Alvaro Machaca](https://github.com/AlvaroMachaca0503) – Estudiante de Ingeniería de Software 🧠
