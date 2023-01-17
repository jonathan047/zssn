from django.urls import path
from . import views
urlpatterns = [
    path('', views.sobreviventes, name="sobreviventes"),
    path('atualiza_sobrevivente/', views.att_sobrevivente, name="atualiza_sobrevivente"),
    path('update_sobrevivente/<int:id>', views.update_sobrevivente, name="update_sobrevivente")
]
