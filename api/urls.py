from django.urls import path, include
from api import views
urlpatterns = [
	path('Hello-view/', views.HelloApiView.as_view())
]
