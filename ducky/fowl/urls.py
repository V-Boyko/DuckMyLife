from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.frontpage, name="frontpage"),
    path("frontpage/", views.frontpage, name="welcome"),
    path("editor/", views.editor, name='editor')
]

# note to test push
# adding one more comment

# Vlads adjusted Code
