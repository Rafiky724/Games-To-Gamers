from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=''),
    path('control/', views.controlGame, name='control'),
    # path('registrarCurso/', views.registrarCurso),
    # path('edicionCurso/<codigo>', views.edicionCurso),
    # path('editarCurso/', views.editarCurso),
    # path('eliminacionCurso/<codigo>', views.eliminarCurso),
]