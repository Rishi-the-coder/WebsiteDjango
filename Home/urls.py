from django.contrib import admin
from django.urls import path
from Home import views #imports views

#from there it will come here
urlpatterns = [
    path("",views.index,name='Home'), # if somenone comes with this url send him to views 's index function and name ths path Home ,... Now we gonna create this function in views
    path("about",views.about,name='About'), #if we write /about 
    path("contacts",views.contacts,name='Contacts'),
    path("sdownload",views.sdownload,name='Sdownload'),
    path("mdownload",views.mdownload,name='Mdownload'),
    path("download",views.download,name='Download'),
    path("game",views.game,name='Game')
]

