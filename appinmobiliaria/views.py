from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'appinmobiliaria/index.html') 

def about(request):
    return render(request, 'appinmobiliaria/about.html')

def pagina_no_encontrada(request):
    return render(request, 'appinmobiliaria/404.html')

def contact(request):
    return render(request, 'appinmobiliaria/contact.html')