from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from silabos.views import (
    DocenteViewSet,
    CarreraViewSet,
    SilaboViewSet,
    UnidadDidacticaViewSet,
    ContenidoViewSet,
    EvaluacionViewSet,
    BibliografiaViewSet
)

router = routers.DefaultRouter()
router.register(r'docentes', DocenteViewSet)
router.register(r'carreras', CarreraViewSet)
router.register(r'silabos', SilaboViewSet)
router.register(r'unidades', UnidadDidacticaViewSet)
router.register(r'contenidos', ContenidoViewSet)
router.register(r'evaluaciones', EvaluacionViewSet)
router.register(r'bibliografia', BibliografiaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
] 