from django.urls import path
from . import views

urlpatterns = [
    path('', views.voting_data, name='voting-data'),
]