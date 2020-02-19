from django.urls import path
from .views import (
    index,
    login
)

urlpatterns = [
    path('', index),
    path('login/', login, name='login'),
    path('new/', newUser, name='new'),
    path('logout/', logout, name='logout'),
    path('reset-password/', resetPassowrd, name='reset-password'),
    path('profile/', profile, name='profile'),

]
