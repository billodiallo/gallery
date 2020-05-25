from django.shortcuts import render
from django.http import HttpResponse, Http404 #RESPONSIBLE to returning a response to user
import datetime as dt  
from .models import Image,Location,Photographer,Category
#Create your views here
def fashion(request):
    images = Image.objects.all()
    return render(request, 'fashion.html',{'images':images})

