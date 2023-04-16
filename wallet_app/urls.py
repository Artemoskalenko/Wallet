from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('json', views.json_view),
    path('check', views.check),
    path('change', views.change),
]