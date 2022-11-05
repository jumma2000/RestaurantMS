from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'configrate/header.html')


def get_user(request):
    return render(request,'configrate/user.html')