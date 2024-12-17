from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', index,name='index'),
    path('studentregister/', views.studentreg,name='studentregister'),
    path('studentlogin/',views.studentlog,name='studentlogin'),
    path('adminlogin/',views.adminlog,name='adminlogin'),
    path('parentregister/',views.parentreg,name='parentregister'),
    path('parentlogin/',views.parentlog,name='parentlogin'),
    path('matronlogin/',views.matronlog,name='matronlogin'),
    path('matrondash/',views.matrondash,name='matrondash'),
    path('studentlistmatron/',views.liststudentsmatron,name='studentlistmatron'),
    path('parentlistmatron/',views.listparentsmatron,name='parentlistmatron'),


    path('admindash/',views.admindash,name='admindash'),
    path('studentlist/',views.liststudents,name='studentlist'),
    path('delstudent/<sid>/',views.delstudent,name='delstudent'),
    path('ediprofile/<sid>/',views.editstudent,name='editstudent'),
    path('editparent/<pid>/',views.editparent,name='editparent'),
    path('about/',views.about,name='about'),
    path('userlogout/',views.logout,name='userlogout'),
    path('parentlist/',views.listparents,name='parentlist'),
]
