from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_app_view(req):
  s = '<h1>This Response is from First App</h1>'

  return HttpResponse(s)