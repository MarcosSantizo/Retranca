from django.shortcuts import render, redirect
from usuarios.models import User

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = User.objects.get(username=username, password=password)
            request.session["user_id"] = user.id
            return redirect("usuarios")
        except User.DoesNotExist:
            return render(request, "login.html", {"form": {"errors": True}})

    return render(request, "login.html")


def logout_view(request):
    request.session.flush()
    return redirect("login")


def creditos(request):
    if "user_id" not in request.session:
        return redirect("login")

    return render(request, "creditos.html")
