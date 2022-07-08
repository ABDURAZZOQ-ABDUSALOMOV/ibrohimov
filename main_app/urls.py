from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('get-code/', get_code, name='get-code'),
    path('enter-code/', enter_code, name='enter-code'),

    path('accounts/login/', enter_code, name='enter-code'),
    path('accounts/register/', enter_code, name='enter-code'),
]
