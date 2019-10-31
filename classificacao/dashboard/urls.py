from django.urls import path
from .views import home, my_logout, login_restrito, logout


urlpatterns = [
    path('', home, name="home"),
    path('login/', login_restrito, name="login"),
    path('logout/', my_logout, name="logout"),
]
