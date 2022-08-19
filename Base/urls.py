from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('about-me/',about_me,name="about_me"),
]
