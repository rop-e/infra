from django.urls import path
from .views import index, index_t

urlpatterns = [
    path('', index),
    path('t/', index_t),
]
