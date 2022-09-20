from django.urls import path
from . import views

app_name = 'productsApp'	# 设置应用名

urlpatterns = [
    path('robot/', views.robot, name='robot'),
    path('monitoring/', views.monitoring, name='monitoring'),
    path('face/', views.face, name='face'),
]
