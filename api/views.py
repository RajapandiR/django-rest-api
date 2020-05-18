from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloApiView(APIView):

	def get(self, request, format = None):

		views = [
			'User HTTP Methods as (get, post, put, delete)',

		]

		return Response({'message': 'Hello', 'views':views})