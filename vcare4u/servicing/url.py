from django.contrib import admin
from django.urls import path,include,re_path
# from knox import views as knox_views
from .view import *
app_name = 'servicing'
urlpatterns = [
        re_path('^validate_phone/', ValidatePhoneSendOTP.as_view()),
        re_path('^validate_otp/',ValidateOTP.as_view()),
        re_path('^register/',Register.as_view()),
        re_path('^login/',LoginAPI.as_view()),
]
