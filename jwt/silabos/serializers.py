from rest_framework import serializers
from .models import (
    Docente,
    Carrera,
    Silabo,
    UnidadDidactica,
    Contenido,
    Evaluacion,
    Bibliografia
)

class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = '__all__'

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = '__all__'

class BibliografiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bibliografia
        fields = '__all__'

class EvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluacion
        fields = '__all__'

class ContenidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contenido
        fields = '__all__'

class UnidadDidacticaSerializer(serializers.ModelSerializer):
    contenidos = ContenidoSerializer(many=True, read_only=True)

    class Meta:
        model = UnidadDidactica
        fields = '__all__'

class SilaboSerializer(serializers.ModelSerializer):
    unidades = UnidadDidacticaSerializer(many=True, read_only=True)
    evaluaciones = EvaluacionSerializer(many=True, read_only=True)
    bibliografia = BibliografiaSerializer(many=True, read_only=True)
    docente_nombre = serializers.CharField(source='docente.nombre', read_only=True)
    carrera_nombre = serializers.CharField(source='carrera.nombre', read_only=True)

    class Meta:
        model = Silabo
        fields = '__all__' 