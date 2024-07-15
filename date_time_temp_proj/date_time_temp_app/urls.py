from django.urls import path
from . import views

urlpatterns = [
  path('date-time/', views.date_time_view)
]