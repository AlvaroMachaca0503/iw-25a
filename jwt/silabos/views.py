from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import (
    Docente,
    Carrera,
    Silabo,
    UnidadDidactica,
    Contenido,
    Evaluacion,
    Bibliografia
)
from .serializers import (
    DocenteSerializer,
    CarreraSerializer,
    SilaboSerializer,
    UnidadDidacticaSerializer,
    ContenidoSerializer,
    EvaluacionSerializer,
    BibliografiaSerializer
)

class DocenteViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['nombre', 'apellidos', 'email']
    filterset_fields = ['titulo_academico']

class CarreraViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'facultad']

class SilaboViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Silabo.objects.all()
    serializer_class = SilaboSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['codigo_curso', 'nombre_curso']
    filterset_fields = ['ciclo', 'carrera', 'docente', 'estado']

class UnidadDidacticaViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = UnidadDidactica.objects.all()
    serializer_class = UnidadDidacticaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['silabo', 'numero']

class ContenidoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Contenido.objects.all()
    serializer_class = ContenidoSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['tema']
    filterset_fields = ['unidad', 'semana']

class EvaluacionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Evaluacion.objects.all()
    serializer_class = EvaluacionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['silabo', 'tipo', 'semana']

class BibliografiaViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Bibliografia.objects.all()
    serializer_class = BibliografiaSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['autor', 'titulo']
    filterset_fields = ['silabo', 'tipo', 'anio'] 