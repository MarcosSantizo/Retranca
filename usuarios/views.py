from django.shortcuts import render, redirect, get_object_or_404
from .models import User


def usuarios_page(request):
    # Validar sesión
    if "user_id" not in request.session:
        return redirect("login")

    usuarios = User.objects.all()

    # Crear usuario dentro de la misma página
    if request.method == "POST":
        User.objects.create(
            username=request.POST["username"],
            password=request.POST["password"]
        )
        return redirect("usuarios")

    return render(request, "usuarios/lista.html", {"usuarios": usuarios})


def crear_usuario(request):
    # Formulario separado usado por "Regístrate"
    if request.method == "POST":
        User.objects.create(
            username=request.POST["username"],
            password=request.POST["password"]
        )
        return redirect("login")  # regresar al login después de registrarse

    return render(request, "usuarios/crear.html")  # plantilla nueva


def eliminar_usuario(request, id):
    if "user_id" not in request.session:
        return redirect("login")

    User.objects.get(id=id).delete()
    return redirect("usuarios")
