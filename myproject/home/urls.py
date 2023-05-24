from django.urls import path,include
from xml.dom.minidom import Document
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.index,name='home'),
]