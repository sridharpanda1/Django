from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

# Create your views here.
def datetime_info_view(request):
  date = datetime.now()
  date_h_m = date.strftime("%H : %S")
  date_hour = date.strftime("%H")
  h = int(date_hour)
  msg = '<h1>Hello Friend...'
  if h < 12:
    msg = msg + ' Good Morning...'
  elif h >= 12 and h <= 16 :
    msg = msg + ' Good After Noon...'
  elif h > 16 and h <= 19:
    msg = msg+' Good Evenging...'
  else: 
    msg = msg+' Good night...'

  msg = msg+'</h1><hr>'
  msg = msg + f'<h1>Server Time is {str(date_h_m)}</h1>'
  print(msg)

  return HttpResponse(msg)