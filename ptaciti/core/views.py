from django.shortcuts import render

# Create your views here.
#class meus_dados()

def my_view(request):
    return render(request,"index.html",)