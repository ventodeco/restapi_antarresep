from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import ResepSerializers, BahanSerializers, KategoriSerializers, ProfilSerializers
from .models import Resep, Bahan, Kategori, Profil



# Create your views here.
@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List, Create Resep' : '/resep/',
		'Detail, Update, Delete Resep' : '/resep/<int:pk>/',

		'List, Create kategori' : '/kategori/',
		'Detail, Update, Delete kategori' : '/kategori/<int:pk>/',

		'List, Create bahan' : '/bahan/',
		'Detail, Update, Delete bahan' : '/bahan/<int:pk>/',

		'List, Create profil' : '/profil/',
		'Detail, Update, Delete profil' : '/profil/<int:pk>/',

	}
	return Response(api_urls)

# Resep views

@api_view(['GET', 'POST'])
def resepList(request):
	if request.method == 'GET':
		reseps = Resep.objects.all()
		serializer = ResepSerializers(reseps, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = ResepSerializers(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def resep(request, pk):
	try:
		resep = Resep.objects.get(id=pk)
	except Resep.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = ResepSerializers(resep)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = ResepSerializers(resep, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		resep.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


# Bahan views

@api_view(['GET', 'POST'])
def bahanList(request):
	if request.method == 'GET':
		bahans = Bahan.objects.all()
		serializer = BahanSerializers(bahans, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = BahanSerializers(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def bahan(request, pk):
	try:
		bahan = Bahan.objects.get(id=pk)
	except Bahan.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = BahanSerializers(bahan)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = BahanSerializers(bahan, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		bahan.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

# Kategori Views

@api_view(['GET', 'POST']) 
def kategoriList(request):
	if request.method == 'GET':
		kategoris = Kategori.objects.all()
		serializer = KategoriSerializers(kategoris, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = KategoriSerializers(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def kategori(request, pk):
	try:
		kategori = Kategori.objects.get(id=pk)
	except Kategori.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = KategoriSerializers(kategori)
		return Response(serializer.data)

	elif request.method =='PUT':
		serializer = KategoriSerializers(kategori, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		kategori.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

# Profil Views

@api_view(['GET', 'POST']) 
def profilList(request):
	if request.method == 'GET':
		profils = Profil.objects.all()
		serializer = ProfilSerializers(kategoris, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = ProfilSerializers(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def profil(request, pk):
	try:
		profil = Profil.objects.get(id=pk)
	except Profil.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = ProfilSerializers(profil)
		return Response(serializer.data)

	elif request.method =='PUT':
		serializer = ProfilSerializers(profil, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		profil.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

