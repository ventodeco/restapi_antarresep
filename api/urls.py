from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('resep/', views.resepList, name="resepList"),
	path('resep/<int:pk>/', views.resep, name="resep"),

	path('bahan/', views.bahanList, name="bahanList"),
	path('bahan/<int:pk>/', views.bahan, name="bahan"),

	path('kategori/', views.kategoriList, name="kategoriList"),
	path('kategori/<int:pk>/', views.kategori, name="kategori"),

	path('profil/', views.profilList, name="profil"),
	path('profil/<int:pk>/', views.profil, name="profil"),
]
