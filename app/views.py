from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def country(request):
    QLTO=Country.objects.all()
    d={'QLTO':QLTO}
    return render(request,'country.html',d)
def capital(request):
    QLTO=Capital.objects.all()
    d={'QLTO':QLTO}
    return render(request,'capital.html',d)

def insert_country(request):
    ci=int(input('enter'))
    cn=input('enter name')
    CNO=Country.objects.get_or_create(country_id=ci,cname=cn)[0]
    CNO.save()
    return HttpResponse('inserted successfully')

def insert_capital(request):
    cid=int(input('enter'))
    caid=int(input('enter capital id'))
    can=input('enter name')
    CNO=Country.objects.get(country_id=cid)
    CAO=Capital.objects.get_or_create(country_id=CNO,capital_id=caid,capital_name=can)[0]
    CAO.save()
    return HttpResponse('inserted successfully')