from django.shortcuts import render
import datetime
from django.http import HttpResponse

# Create your views here.
def get_time_view(request):
  time = datetime.datetime.now()
  s = f'<h1>The Current Server Date and Time is {time} </h1>'
  return HttpResponse(s)

