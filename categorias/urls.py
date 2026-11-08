from django.urls import path
from .views import listar_categorias

urlpatterns = [path('categorias/', listar_categorias),]

from .views import listar_categorias, listar_categorias_despesas

urlpatterns = [path('categorias/', listar_categorias),path('categorias/despesas/', listar_categorias_despesas),]