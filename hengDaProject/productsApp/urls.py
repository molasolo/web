from django.urls import path
from . import views

app_name = 'productsApp'

urlpatterns = [
    path('robot/', views.robot, name='robot'),
    path('monitoring/', views.monitoring, name='monitoring'),
    path('face/', views.face, name='face'),
]
