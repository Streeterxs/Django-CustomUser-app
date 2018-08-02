from django.urls import path
from authenticator import views

app_name='auth'
urlpatterns = [
    path('login', views.loginning, name='login'),
    path('signup', views.signup, name='signup')
]
