from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=''),
    path('control/', views.controlGame, name = 'control'),
    path('registerGame/', views.registerGame, name = 'register'),
    path('editGame/<codigo>/', views.editGame, name = 'edit'),
    path('gameEdition/', views.gameEdition, name = 'game'),
    path('deleteGame/<codigo>/', views.deleteGame, name = 'delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)