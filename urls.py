from django.urls import path, include

from . import views

app_name = 'space'

urlpatterns = [
    path('', views.index, name='pagina-inicial'),
    path('categorias/', views.categorias, name='categorias'),
    path('categorias/<slug:action>/', views.categorias, name='manage-categoria'),
    path('categorias/<int:oid>/<slug:action>/', views.categorias, name='manage-categoria'),

    path('localizadores/', views.localizacoes, name='manage-localizador'),
    path('localizadores/<int:oid>/', views.localizacoes, name='manage-localizador'),

    path('espacos/', views.espacos, name='espacos'),
    path('espacos/<int:oid>/', views.espacos, name='espacos'),

    path('gestores/', views.gestores, name='gestores'),
    path('gestores/<slug:action>/', views.gestores, name='manage-gestores'),
    path('gestores/<int:oid>/<slug:action>/', views.gestores, name='manage-gestores'),

    path('reservas/', views.reservas, name='reservas'),
    path('reservas/<slug:action>/', views.reservas, name='manage-reservas'),

    path('json/', views.events, name='events')
]
