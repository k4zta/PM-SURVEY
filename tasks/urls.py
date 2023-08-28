from django.urls import path
from .views import vista
from.views import iniciar_sesion

urlpatterns = [path("", vista), path("", iniciar_sesion)]