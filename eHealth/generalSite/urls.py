from django.conf.urls import patterns, include, url
from django.contrib import admin
from generalSite import views

urlpatterns = (
    
    url(r'^$', views.index, name="indexfunc"),
    url(r'^generalSite', views.index, name="indexfunc"),
    
    )