from django.urls import path
from .views import FilterCreateAPI, CategoryAPI, UserFilterAPI, PriceListAPI, PercentAPI

urlpatterns = [
    path('', FilterCreateAPI.as_view()),
    path('categories/', CategoryAPI.as_view()),
    path('user/', UserFilterAPI.as_view()),
    path('percent/', PercentAPI.as_view()),
    path('price/list/', PriceListAPI.as_view())
]
