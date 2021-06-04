from django.urls import path
from . import views

# added for ajax
from django.conf.urls import url



urlpatterns = [
    path('', views.index),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),

    # added for ajax
    url(r'^validate_email/$', views.validate_email, name='validate_email'),
    url(r'^validate_username/$', views.validate_username, name='validate_username'),
]
