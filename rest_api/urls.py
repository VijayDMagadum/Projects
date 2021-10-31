from django.urls import path

from . import views


urlpatterns = [
    path('',views.index),
    path('login/',views.login),
    path('reg/',views.reg),
     path('adminlog/',views.adminlog,name="userpage"),
     path('update/',views.update,name='update'),
     path('delete/',views.delete,name="delete"),

]