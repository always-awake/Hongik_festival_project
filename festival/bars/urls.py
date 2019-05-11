from django.urls import path
from . import views


app_name = 'bars'
urlpatterns = [
    path('', views.bar_list, name='bar_list')
]
