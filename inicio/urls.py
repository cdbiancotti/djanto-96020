from django.urls import path
from inicio.views import inicio, vista2

urlpatterns = [
    path('', inicio),
    path('vista2/', vista2)
]
