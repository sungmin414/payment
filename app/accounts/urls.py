from .views import profile, auth_login
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_login, name='login'),
    path('profile/', profile, name='profile'),

]