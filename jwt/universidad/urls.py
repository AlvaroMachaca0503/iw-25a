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
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
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
    # JWT Authentication endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # API endpoints
    path('api/', include(router.urls)),
] 