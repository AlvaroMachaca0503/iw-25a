from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Docente(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField()
    titulo_academico = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

class Carrera(models.Model):
    nombre = models.CharField(max_length=100)
    facultad = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Silabo(models.Model):
    # Información General
    codigo_curso = models.CharField(max_length=20, unique=True)
    nombre_curso = models.CharField(max_length=200)
    ciclo = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    creditos = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
    horas_teoricas = models.IntegerField(default=0)
    horas_practicas = models.IntegerField(default=0)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    
    # Sumilla
    sumilla = models.TextField()
    
    # Competencias
    competencia_general = models.TextField()
    competencias_especificas = models.TextField()
    
    # Requisitos
    prerequisitos = models.CharField(max_length=200, blank=True)
    
    # Estado y fechas
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    estado = models.CharField(
        max_length=20,
        choices=[
            ('borrador', 'Borrador'),
            ('revision', 'En Revisión'),
            ('aprobado', 'Aprobado'),
            ('publicado', 'Publicado')
        ],
        default='borrador'
    )
    
    def __str__(self):
        return f"{self.codigo_curso} - {self.nombre_curso}"

class UnidadDidactica(models.Model):
    silabo = models.ForeignKey(Silabo, on_delete=models.CASCADE, related_name='unidades')
    numero = models.IntegerField()
    titulo = models.CharField(max_length=200)
    duracion_semanas = models.IntegerField()
    competencias = models.TextField()
    
    def __str__(self):
        return f"Unidad {self.numero}: {self.titulo}"

class Contenido(models.Model):
    unidad = models.ForeignKey(UnidadDidactica, on_delete=models.CASCADE, related_name='contenidos')
    tema = models.CharField(max_length=200)
    subtemas = models.TextField()
    semana = models.IntegerField()
    
    def __str__(self):
        return self.tema

class Evaluacion(models.Model):
    silabo = models.ForeignKey(Silabo, on_delete=models.CASCADE, related_name='evaluaciones')
    tipo = models.CharField(
        max_length=50,
        choices=[
            ('parcial', 'Examen Parcial'),
            ('final', 'Examen Final'),
            ('practica', 'Práctica Calificada'),
            ('trabajo', 'Trabajo'),
            ('otros', 'Otros')
        ]
    )
    descripcion = models.CharField(max_length=200)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    semana = models.IntegerField()
    
    def __str__(self):
        return f"{self.tipo} - Semana {self.semana}"

class Bibliografia(models.Model):
    silabo = models.ForeignKey(Silabo, on_delete=models.CASCADE, related_name='bibliografia')
    tipo = models.CharField(
        max_length=20,
        choices=[
            ('basica', 'Básica'),
            ('complementaria', 'Complementaria')
        ]
    )
    autor = models.CharField(max_length=200)
    titulo = models.CharField(max_length=300)
    anio = models.IntegerField()
    editorial = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.titulo} ({self.anio})" 