from django.urls import path

from .views import ProcesarView


urlpatterns = [
    path('imagenes/', ProcesarView.as_view(), name='imagenes_list'),
    path('agregar_imagen/', ProcesarView.as_view(), name='add_image'),
    path('imagenes/<int:id>/', ProcesarView.as_view(), name='imagenes_process'),
    path('imagen_eliminar/<int:id>/', ProcesarView.as_view(), name='imagenes_delete'),
    path('imagenes/<int:id>/<int:id_step>', ProcesarView.as_view(), name='imagenes_process_step'),
]
