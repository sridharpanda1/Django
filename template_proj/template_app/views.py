from django.shortcuts import render

	# Create your views here.
def wish(req):
	return render(req, 'static/index.html')
