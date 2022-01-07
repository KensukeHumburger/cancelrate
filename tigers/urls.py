from django.urls import path
from . import views

app_name= 'tigers'

urlpatterns = [
    path('', views.index, name='index'),
    path('predict_input/', views.predict_input, name='predict_input'),
    path('predict/', views.predict, name='predict'),
]
