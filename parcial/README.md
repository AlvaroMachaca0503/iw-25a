```markdown
# Parcial - Ingeniería Web

Este es el proyecto de scaffolding con Flask y Docker para el parcial de Ingeniería Web.

## Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
```

_Reemplaza_ `https://github.com/tu-usuario/tu-repo.git` por tu URL real en GitHub.

---

## Ejecutar con Docker

1. **Construir la imagen** (sin usar cache para evitar restos de compilaciones anteriores):

   ```bash
   docker-compose build --no-cache web
   ```

2. **Levantar los contenedores**:

   ```bash
   docker-compose up
   ```

3. El panel de administración estará disponible en  
   `http://localhost:5000/admin`

> El servicio `db` (PostgreSQL) y `web` (tu app Flask) se levantan juntos.

---

## Ejecutar en local (SQLite)

1. **Configurar `config.py`**  
   En el bloque de la URI de base de datos, **descomenta** la parte de SQLite:

   ```python
   import os

   class Config:
       SQLALCHEMY_DATABASE_URI = os.getenv(
           'DATABASE_URL',
           f"sqlite:///{os.path.abspath(os.path.dirname(__file__))}/app.db"
       )
       SQLALCHEMY_TRACK_MODIFICATIONS = False
   ```

2. **Instalar dependencias** (virtualenv):

   ```bash
   python -m venv env
   source env/bin/activate      # macOS/Linux
   env\Scripts\activate         # Windows PowerShell
   pip install -r requirements.txt
   ```

3. **Inicializar migraciones**:

   ```bash
   flask db init
   ```

4. **Generar una migración**:

   ```bash
   flask db migrate -m "Migrando modelos"
   ```

5. **Aplicar migraciones**:

   ```bash
   flask db upgrade
   ```

6. **Correr la aplicación**:

   ```bash
   python app.py
   ```

   Luego abre `http://127.0.0.1:5000/admin` en tu navegador.

```