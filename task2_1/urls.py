from django.urls import path
from . import views

urlpatterns = [
    path('', views.home1,name="home1"),
    path('login/',views.login1,name='login1'),

]