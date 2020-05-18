from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api import serializers
from rest_framework import status
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
