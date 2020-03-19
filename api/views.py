from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import ResepSerializers
from .models import Resep



# Create your views here.
@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List Resep' : '/resep/',
		'Detail Resep' : '/resep/<int:pk>/',
		'Create Resep' : '/resep/',
		'Update Resep' : '/resepUpdate/<int:pk>/',
		'Delete Resep' : '/resepDelete/<int:pk>/'
	}
	return Response(api_urls)

@api_view(['GET'])
def resepList(request):
	reseps = Resep.objects.all()
	serializer = ResepSerializers(reseps, many=True)
	return Response(serializer.data)

@api_view(['POST'])
def resepCreate(request):
	serializer = ResepSerializers(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def resep(request, pk):
	try:
		resep = Resep.objects.get(id=pk)
	except Resep.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'POST':
		serializer = ResepSerializers(data=request)
		if serializer.is_valid():
			serializer.save()
		return Response(serializer.data)

	elif request.method == 'GET':
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


