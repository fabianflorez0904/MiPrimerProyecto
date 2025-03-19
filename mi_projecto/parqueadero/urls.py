from django.urls import path
from .views import lista_parqueaderos, agregar_parquedero, editar_parqueadero, eliminar_parqueadero, registro

urlpatterns = [
    path('', lista_parqueaderos, name='lista_parqueaderos'),
    path('agregar/', agregar_parquedero, name="agregar_parqueadero"),
    path('editar/<int:pk>/', editar_parqueadero, name='editar_parqueadero'),
    path('eliminar/<int:pk>/', eliminar_parqueadero, name='eliminar_parqueadero'),
    path('registo/', registro, name='registro')
]
