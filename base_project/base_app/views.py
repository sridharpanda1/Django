from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_view(req):
  return HttpResponse('<h1>1st View</h1>')

def second_view(req):
  return HttpResponse('<h1>2nd View</h1>')

def third_view(req):
  return HttpResponse('<h1>3rd View</h1>')

def fouth_view(req):
  return HttpResponse('<h1>4th View</h1>')

def fifth_view(req):
  return HttpResponse('<h1>5th View</h1>')