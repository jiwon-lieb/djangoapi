from django.urls import path, include
from . import views
from rest_framework import routers # GET and POST requests

router = routers.DefaultRouter()
router.register('courses', views.CourseView)

urlpatterns = [
    path('', include(router.urls)),
    
]