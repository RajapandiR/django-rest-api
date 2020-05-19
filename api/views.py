from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

from api import serializers
from api import models
from api import permissions

# Create your views here.

class HelloApiView(APIView):
	serializer_class = serializers.HelloSerializers
	def get(self, request, format = None):

		views = [
			'User HTTP Methods as (get, post, put, delete)',

		]

		return Response({'message': 'Hello', 'views':views})

	def post(self, request):
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			name = serializer.validated_data.get('name')
			message = f'Hello {name}'
			return Response({'message':message})
		else:
			return Response(
				serializer.errors,
				status = status.HTTP_400_BAD_REQUEST
				)

	def put(self, request):
		return Response({'message': 'PUT'})

	def patch(self, request):
		return Response({'message': 'PATCH'})

	def delete(self, request):
		return Response({'message': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
	serializer_class = serializers.HelloSerializers

	def list(self, request):
		viewset = [
			'User actions create, read, update, destroy, list'
		]
		return Response({'message': 'Hello', 'viewset': viewset})

	def create(self, request):
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			name = serializer.validated_data.get('name')
			message = f'Hello {name}'
			return Response({'message':message})
		else:
			return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

	def retrieve(self, request, pk=None):
		return Response({'HTTP-Method': 'GET'})

	def update(self, request, pk=None):
		return Response({'HTTP-Method': 'PUT'})

	def destroy(self, request, pk=None):
		return Response({'HTTP-Method': 'DELETE'})

class StudViewSet(viewsets.ModelViewSet):
	serializer_class = serializers.StudSerializers
	queryset = models.Stud.objects.all()
	authentication_classes = (TokenAuthentication,)
	permission_classes = (permissions.UpdateOwnStud,)
 