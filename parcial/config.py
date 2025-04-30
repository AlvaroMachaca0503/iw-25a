import os

class Config:
    # Docker con postgres
    # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    
    # Sql lite en local
    """SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        f"sqlite:///{os.path.abspath(os.path.dirname(__file__))}/app.db"  # Esto apunta a app.db en el directorio raíz de la aplicación
    )"""
    #SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Postgresql de manera remota
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'postgresql://postgres:123456789@localhost:5432/bd_scaff'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
