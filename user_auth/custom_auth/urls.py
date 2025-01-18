from django.urls import path
from .views import *

urlpatterns = [
    path('api/register/', register),
    path('api/login/', login),
    path('api/logout/', logout),
    path('api/refresh/', refresh),
    path('api/me/', me),
]
