from django.urls import path, include
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Hello-viewset', views.HelloViewSet, basename='Hello-viewset')
router.register('stud', views.StudViewSet)
router.register('stud-profile', views.StudProfileViewSet)

urlpatterns = [
	path('Hello-view/', views.HelloApiView.as_view()),
	path('login/', views.UserLoginView.as_view()),
	path('', include(router.urls)),
]
