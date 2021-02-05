from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import UserProfileViewSet,accountView,loginView,registerView, verificationView,forget_pass,forget_pass_email_confirm_view,forgot_change,change

router = DefaultRouter()
router.register('profiles',UserProfileViewSet,basename='user-profile-viewset')
app_name = 'users'

urlpatterns = [
    path('',include(router.urls)),
    path('account/',accountView,name='account_profile'),
    path('verification/',verificationView,name='account_email_verification_sent'),
    path('login/',loginView,name='account_login'),
    path('register/',registerView,name='account_signup'),
    path('forgot/',forget_pass,name='forget-pass'),
    path('forgot/confirm/',forget_pass_email_confirm_view,name='forget_pass_email_confirm'),
    # path('forgot-change/<str:uid>/<str:token>/',forgot_change, name="forgot_change" ),
    path('password-change/',change, name="change"),


]
