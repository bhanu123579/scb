# netbanking/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # this is the homepage for the app
    path('login.html', views.login, name='login'),
path('otp_page.html', views.otp_page, name='otp_page'),
path('landing.html', views.landing, name='landing'),
path('estatement_page.html', views.estatement_page, name='estatement_page'),
path('view_estatement_page.html', views.view_estatement_page, name='view_estatement_page'),
]
