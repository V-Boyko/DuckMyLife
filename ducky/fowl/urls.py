from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.base, name="base")
]

# note to test push
# adding one more comment

# Vlads adjusted Code
