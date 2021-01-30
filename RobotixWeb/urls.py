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
from django.conf.urls.static import static
from django.conf import settings
from allauth.account.views import confirm_email
from extras.views import sponsors,sponsors_api
from users.views import verify_user
from rest_framework import routers
from rest_auth.registration.views import VerifyEmailView, RegisterView
from django.contrib.auth.views import LogoutView
from users.views import forgot_change
# from rest_auth.views import LoginView
router = routers.DefaultRouter()
router.register(r'sponsors', sponsors_api)

urlpatterns = [
    path('reset/<str:uid>/<str:token>/',forgot_change, name="forgot_change"),
    path('devtainsaan/', admin.site.urls),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('rest-auth/registration/account-confirm-email/<str:key>/',verify_user, name="verify_user"),
    path('rest-auth/registration/account-confirm-email/',VerifyEmailView.as_view(),name='account_email_verification_sent'),
    # path('verify_user/<str:key>/',verify_user, name="verify_user"),
    path('',views.index,name='index'),
    path('aboutus/',include('about.urls')),
    path('events/',include('events.urls')),
    path('gallery/',include('gallery.urls')),
    path('achievements/',include('achievements.urls')),
    path('contactus/',include('contact.urls')),
    path('info/',include('extras.urls')),
    path('alumni/',include('alumni.urls')),
    path('webteam',views.webteam,name='webteam'),
    path('', include('django.contrib.auth.urls')),
    path('robofest/robothon/',views.robothondetail,name='robothon-detail'),
    path('robofest/roboexpo/',views.roboexpodetail,name='roboexpo-detail'),
    path('robofest/',views.robofestdetail,name='robofest-detail'),
    # path('accounts/',include('allauth.urls')),
    # path('form',views.form,name='form'),
    path('accounts/',include('users.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('rest-auth/',include('rest_auth.urls')),
    path('robothon/',include('roboPortal.urls')),
    path('roboexpo/',include('roboexpo.urls')),
    path('sponsors/',sponsors, name= "sponsors"),
    path('',include('workshops.urls')),

    # path('accounts-rest/registration/account-confirm-email/<key>/', LoginView.as_view(), name='account_confirm_email'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Robotix Club NIT Raipur"
admin.site.site_title = "Robotix Club NIT Raipur"
admin.site.index_title = "Robotix Club NIT Raipur"
