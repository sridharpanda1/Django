from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def second_app_view(req):
  s = '<h1>This Response is from Second App</h1>'

  return HttpResponse(s)
