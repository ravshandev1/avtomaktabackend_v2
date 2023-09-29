from rest_framework import generics, response, views
from .models import Price, Percent
from .serializers import CategorySerializer, PriceSerializer, PercentSerializer
from instructor.serializers import InstructorSerializer
from instructor.models import Instructor
from client.models import Category


class PercentAPI(generics.ListAPIView):
    queryset = Percent.objects.all()
    serializer_class = PercentSerializer


class PriceListAPI(generics.ListAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer

    def get_queryset(self):
        qs = self.queryset.filter(category__instructors__balans__isnull=False)
        return qs.order_by('category').distinct('category')


class CategoryAPI(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class FilterCreateAPI(generics.ListAPIView):
    queryset = Instructor.objects.filter(tasdiqlash=True)
    serializer_class = InstructorSerializer

    def get_queryset(self):
        qs = self.queryset.order_by('tuman').distinct('tuman')
        tum = self.request.query_params.get('tum')
        if tum:
            qs = self.queryset.filter(tuman__exact=tum)
        return qs


class UserFilterAPI(views.APIView):
    def get_queryset(self):
        tg_id = self.request.query_params.get('id')
        ins = Instructor.objects.filter(telegram_id=tg_id).filter()
        if ins:
            return "Instructor"
        else:
            return "Not registered"

    def get(self, request, *args, **kwargs):
        return response.Response({'message': self.get_queryset()})
