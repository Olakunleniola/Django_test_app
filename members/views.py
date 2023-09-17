#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
# Create your views here.

def members(request):
    mychildren = Member.objects.all().values()
    template = loader.get_template("mychildren.html")
    context = {
        'omomi' : mychildren
    }
    return HttpResponse(template.render(context,request))

def details(request, name):
    child = Member.objects.get(lastname=name)
    template = loader.get_template("details.html")
    context = {
        "omo":child
    }
    return HttpResponse(template.render(context,request))

def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())

def test(request):
    template = loader.get_template("test.html")
    context = {
        "fruits" : ["Apple", "Pawpaw", "Water-melon", "Cherry"]
    }
    return HttpResponse(template.render(context,request))

