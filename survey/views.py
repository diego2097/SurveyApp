from django.shortcuts import render,redirect

def index(request):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, "survey/index.html")
    # En otro caso redireccionamos al login
    return redirect('/accounts/login')
