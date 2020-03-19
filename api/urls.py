from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('resep/', views.resepList, name="resepList"),
	path('resep/<int:pk>/', views.resep, name="resep"),
]
