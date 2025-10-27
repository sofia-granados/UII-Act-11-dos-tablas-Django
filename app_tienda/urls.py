from django.urls import path
from . import views

app_name = 'app_tienda'

urlpatterns = [
    path('', views.listar_animales, name='listar_animales'),
    path('animal/<int:animal_id>/', views.detalle_animal, name='detalle_animal'),
    path('crear/', views.crear_animal, name='crear_animal'),
    path('editar/<int:animal_id>/', views.editar_animal, name='editar_animal'),
    path('borrar/<int:animal_id>/', views.borrar_animal, name='borrar_animal'),
]