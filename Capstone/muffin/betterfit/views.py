from django.shortcuts import render

# Create your views here.
# def index(request):
#    return HttpResponse("Hello, world. You're at the betterfit index.")

def home(request):
    return render(request, 'home.html', {})

def generic(request):
    return render(request, 'generic.html', {})

def elements(request):
    return render(request, 'elements.html', {})
