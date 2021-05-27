from django.shortcuts import render

# Create your views here.
# def index(request):
#    return HttpResponse("Hello, world. You're at the betterfit index.")
from betterfit.models import User


def home(request):
    print(111, request.POST)
    if request.method=="POST":

        clothes_img=request.FILES["clothes_img"]
        #outer_img=request.FILES["outer_img"]
        pants_img=request.FILES["pants_img"]

        muffin=User.objects.create_user(clothes_img)
        muffin.clothes_img=clothes_img
        #user.outer_img=outer_img
        muffin.pants_img=pants_img
        muffin.save()





    return render(request, "home.html", {})




def generic(request):



    return render(request, 'generic.html', {})

def elements(request):
    return render(request, 'elements.html', {})



from django.shortcuts import render


def mannequin(request):
    return render(request, 'mannequin.html', {})

