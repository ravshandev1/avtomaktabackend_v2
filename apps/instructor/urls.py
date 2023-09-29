from django.urls import path
from .views import InstructorAPI, CarListAPI, RegionListAPI, TextRAPI, TextUAPI

urlpatterns = [
    path('<int:pk>/', InstructorAPI.as_view()),
    path('regions/', RegionListAPI.as_view()),
    path('cars/', CarListAPI.as_view()),
    path('text-r/<int:pk>/', TextRAPI.as_view()),
    path('text-u/<int:pk>/', TextUAPI.as_view()),
]
