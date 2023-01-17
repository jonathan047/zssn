from django.urls import path
from . import views
urlpatterns = [
    path('relatorio_geral/', views.relatorio_geral, name="relatorio_geral"),
    path('atualiza_sobrevivente/', views.att_sobrevivente, name="atualiza_cliente")
]
