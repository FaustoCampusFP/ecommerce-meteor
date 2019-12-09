from django.urls import path
from .views import *

app_name = 'ecommerce'

urlpatterns = [
    path('', home, name='home'),
    path('catalogo/', catalog, name='catalog'),
    path('catalogo/<int:pk>/', detail, name='detail'),
]
