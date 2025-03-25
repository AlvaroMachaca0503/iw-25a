# Lab02 - Ingeniería Web  

## 📂 Contenido del repositorio  
Este repositorio incluye los archivos necesarios para la configuración y despliegue de una aplicación web en un entorno **Docker**.  

Estructura del proyecto:  
- 📂 `css/` → Archivos de estilos CSS. 
- 📂 `js/` → Archivos JavaScript para la interactividad.  
- 📄 `lab01.html` → Archivo principal HTML de la aplicación.  
- 📄 `Dockerfile` → Configuración para crear la imagen Docker de la aplicación.  
- 📄 `default.conf` → Configuración para el servidor web dentro del contenedor.  

## 🚀 Tecnologías utilizadas  
- **HTML5** para la estructura del documento.  
- **CSS3** para los estilos y diseño.  
- **JavaScript** para la interactividad.  
- **Docker** para la contenedorización y despliegue de la aplicación.  
- **NGINX** como servidor web dentro del contenedor.  

## 🛠️ Instrucciones para ejecutar el proyecto  
1. Clona el repositorio en tu equipo:
   git clone  https://github.com/AlvaroMachaca0503/iw-25a.git
   cd iw-25a/lab2

2. Construye la imagen Docker con el siguiente comando:
   docker build -t test01_lab2 .

3. Ejecuta el contenedor utilizando:
   docker run -d -p 8088:80 test01_lab2

4. Abre tu navegador y accede a la aplicación en:
   http://localhost:8088

   📌 Notas
Asegúrate de tener Docker instalado en tu sistema.
Revisa el archivo default.conf para ajustar la configuración de NGINX según sea necesario.
