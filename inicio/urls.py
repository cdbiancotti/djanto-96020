from django.urls import path
from inicio.views import inicio, vista2

app_name = 'inicio'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('vista2/', vista2, name='condicional_y_bucle')
]
