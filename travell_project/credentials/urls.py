from django.urls import path

from . import views

urlpatterns=[
    path('register',views.register,name="register"),
    path('reg_index', views.reg_index, name="reg_index"),
    path('login', views.login, name="login"),
    path('login1', views.login1, name="login1"),

    path('logout',views.logout,name="logout"),


]