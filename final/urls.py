from django.contrib import admin
from django.urls import path, include
from core.views import login_view, logout_view, creditos
from usuarios.views import usuarios_page, eliminar_usuario, crear_usuario

urlpatterns = [
    path("admin/", admin.site.urls),

    # Rutas de usuarios
    path("usuarios/", include("usuarios.urls")),

    # Página principal será lista de usuarios
    path("", include("usuarios.urls")),

    # Login - Logout
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),

    # Créditos
    path("creditos/", creditos, name="creditos"),

    path("usuarios/crear/", crear_usuario, name="crear_usuario"),

]

