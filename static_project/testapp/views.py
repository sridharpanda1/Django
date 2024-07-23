from django.shortcuts import render

# Create your views here.
def display_flower(req):
  flower = {'f1':"Rose", 'f2':"Lilly", 'f3':"Sunflower"}
  return render(req, 'testapp/display.html', flower)