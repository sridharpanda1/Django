from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hyd_jobs_info(request):
  s = '<h1>Hydrabad jobs inforamtion will be listed here.</h1>'
  return HttpResponse(s)

def blore_jobs_info(request):
  s = '<h1>Banglore jobs inforamtion will be listed here.</h1>'
  return HttpResponse(s)

def pune_jobs_info(request):
  s = '<h1>Pune jobs inforamtion will be listed here.</h1>'
  return HttpResponse(s)

def bbsr_jobs_info(request):
  s = '<h1>Bhubanewar jobs inforamtion will be listed here.</h1>'
  return HttpResponse(s)