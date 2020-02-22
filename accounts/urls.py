from django.urls import path
from .views import (
    #index,
    LoginView,
    #logout,
    new_user,
    ProfileView,
    #reset_password
)

urlpatterns = [
    #path('', index),
    path('new/', new_user, name='new_user'),
    path('login/', LoginView.as_view(), name='login'),
    #path('logout/', logout, name='logout'),
    #path('reset-password/', reset_password, name='reset-password'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),

]
