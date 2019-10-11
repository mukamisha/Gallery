from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Image,Category,Location

# Create your views here.
# def welcome(request):
#     return HttpResponse('Welcome to the Moringa Tribune')


def images(request):
   images = Image.objects.all()
   return render(request, 'image.html',{'images':images})