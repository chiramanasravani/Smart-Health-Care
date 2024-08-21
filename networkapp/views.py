from django.shortcuts import render

# Create your views here.


from turtle import down
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from userapp.models import *
from mainapp.models import *
from cloudapp.models import *

from django.db.models import Q
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
import requests
import random
import numpy as np
import matplotlib.pyplot as plt

from django.core.mail import EmailMultiAlternatives
from healthproject.settings import DEFAULT_FROM_EMAIL
from mainapp.check_internet import *
from networkapp.models import *
from mainapp.check_internet import *
from networkapp.models import *
from protectionapp.models import *
from cryptography.fernet import Fernet
# from Power.settings import DEFAULT_FROM_EMAIL
# import pandas as pd

def nm_login(request):
    if request.method=='POST':
        name=request.POST.get('name')
        pwd=request.POST.get('pwd')
        if name=='network' and pwd=='network':
            messages.info(request,"login successfull")
            return redirect('nm_dashboard')
        else:
            messages.warning(request,'Something Wrong, Please try again.')
            print('message')
            return redirect ('nm_login')
    return render(request,'main/nm-login.html')



def nm_dashboard(request):
    users=userModel.objects.count()
    device=deviceModel.objects.count()
    phi=phiModel.objects.count()
    data1 = phiModel.objects.filter(status='Pending').count()
    print(data1)
    data2 = phiModel.objects.filter(phi_status="Pending").count()
    print(data2)
    data3 = deviceModel.objects.filter(device_status='Pending').count()
    return render(request,'network-manager/nm-dashboard.html',{'users':users,'device':device,'phi':phi,'data1':data1,'data2':data2,'data3':data3})
  


def nm_view_pad_details(request):

    data=deviceModel.objects.all().order_by("-device_id")
    if request.method=='POST':
         search=request.POST.get('search')
         data=deviceModel.objects.filter(Q(device_id__icontains=search))
    return render(request,'network-manager/nm-view-pad-details.html',{'data':data})    


def accept_status(request,id):
    accept=get_object_or_404(deviceModel,device_id=id)
    accept.key_status='Sended'
    accept.save(update_fields=['key_status'])
    accept.save()

    print("okkkkkkkkkkkkkkk")
    key = Fernet.generate_key()
    print(key)
    file_key = key.decode()
    print(file_key)
    deviceModel.objects.filter(device_id=id).update(nm_key=file_key)
    messages.info(request,'Key successfully Sended.')

    return redirect('nm_view_pad_details')
