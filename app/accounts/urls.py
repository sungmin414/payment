from .views import profile, auth_login, login_info
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_login, name='login'),
    path('profile/', profile, name='profile'),
    path('login_info/', login_info, name='login_info')

]