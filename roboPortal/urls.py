"""RobotixWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
app_name = 'robothon'
urlpatterns = [
    path('registration/',views.home,name= "home"),
    path('registration/api/',views.home_api,name= "home_api"),
    path('problem-statements/',views.problem_statements,name='problem-statement'),
    path('problem-statements/api/',views.problem_statements_api,name='problem-statement-api'),
    # path('register/',views.register,name="register"),
    # path('login/',views.login, name="login"),
    # path('verify/<str:token>/<int:id>/',views.verify,name="verify"),
    path('createProfile/', views.createProfile, name="createProfile"),
    path('adminView/',views.adminView, name= "adminView"),
    path('profileView/<int:user_id>/',views.profileView, name= "profileView"),
    path('select/<int:team_id>',views.select, name="select"),
    path('confirm/<str:token>/',views.confirm, name="confirm"),

    #path('create/',views.create, name= "create"),
    #path('email/',views.email,name="email"),
]
