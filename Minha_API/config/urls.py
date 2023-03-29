from django.contrib import admin
from django.urls import path, include
from empresa.views import FuncionariosViewSet
from rest_framework import routers

#router principal capaz de manipular as informações na API
router = routers.DefaultRouter()

router.register(r'funcionarios', FuncionariosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
