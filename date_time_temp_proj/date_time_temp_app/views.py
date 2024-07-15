from django.shortcuts import render
import datetime

# Create your views here.
def date_time_view(req):
  date_time = datetime.datetime.now
  date_time_dict = {'date_time': date_time}

  return render(req, 'static/index.html', context=date_time_dict)