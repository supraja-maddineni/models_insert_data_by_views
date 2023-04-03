from django.shortcuts import render
from django.http import HttpResponse
from app.models  import *

# Create your views here.
def insert_Topic(request):
    tn=input('enter topic_name: ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('Topic Inserted Successfully')

def insert_Webpage(request):
    tn=input('enter Topic_name: ')
    name=input('enter name: ')
    url=input('enter url: ')
    email=input('enter email: ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    WO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url,email=email)[0]
    WO.save()
    return HttpResponse('Webpage Data Inserted Successfully')

def insert_AccessRecord(request):
    tn=input('enter Topic_name: ')
    name=input('enter name: ')
    url=input('enter url: ')
    author=input('enter author name: ')
    date=input('enter date: ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    WO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url,email=email)[0]
    WO.save()
    AO=AccessRecord.objects.get_or_create(name=WO,author=author,date=date)[0]
    AO.save()
    return HttpResponse('AccessRecord  Inserted Successfully')

