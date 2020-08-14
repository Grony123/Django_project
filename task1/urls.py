from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home0"),
    path('case/',views.case,name=" case-1")

]