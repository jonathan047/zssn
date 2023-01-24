from django.urls import path
from . import views
urlpatterns = [
    path('infectado/', views.infectado, name="infectado"),
    
]
