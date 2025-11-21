from django.urls import path
from .views import usuarios_page, eliminar_usuario, crear_usuario

urlpatterns = [
    path("", usuarios_page, name="usuarios"),
    path("crear/", crear_usuario, name="crear_usuario"),
    path("eliminar/<int:id>/", eliminar_usuario, name="eliminar_usuario"),
]
