from django.urls import path
from .views import DeleteUserAPI, InformationAPI

urlpatterns = [
    path('delete/<int:pk>/', DeleteUserAPI.as_view()),
    path('info/<int:pk>/', InformationAPI.as_view()),
]
