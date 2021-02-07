from django.contrib import admin
from django.urls import path
from . import views


# django admin customization
admin.site.site_header = "Developer Samuel"
admin.site.site_title = "Welcome to Samuel's Dashbord"
admin.site.index_title = 'Welcome to this portal'

urlpatterns = [
    path('',views.index , name='index'),
    path('about/',views.about , name='about'),
    path('projects/',views.projects , name='projects'),
    path('contact/',views.contact , name='contact'),


]
