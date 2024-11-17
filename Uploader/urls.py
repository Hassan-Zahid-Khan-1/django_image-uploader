from django.urls import path,include
from .views import *


urlpatterns = [
    path('',home,name='home'),


     path("__reload__/", include("django_browser_reload.urls")),
]