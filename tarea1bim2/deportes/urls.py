
from django.urls import path

from deportes import views


urlpatterns = [
        path('', views.acciones, name='acciones'),
 ]
