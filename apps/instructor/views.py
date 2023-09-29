from django.shortcuts import get_object_or_404
from rest_framework import generics, response
from .models import Instructor, Tuman, TextInsUpdater, TextInsRegister
from .serializers import InstructorSerializer, TumanSerializer, TextUpdaterSerializer, TextRegisterSerializer
from session.serializers import MoshinaSerializer
from session.models import Car, Category


class TextRAPI(generics.RetrieveAPIView):
    queryset = TextInsRegister.objects.all()
    serializer_class = TextRegisterSerializer


class TextUAPI(generics.RetrieveAPIView):
    queryset = TextInsUpdater.objects.all()
    serializer_class = TextUpdaterSerializer


class RegionListAPI(generics.ListAPIView):
    queryset = Tuman.objects.all()
    serializer_class = TumanSerializer


class CarListAPI(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = MoshinaSerializer

    def get_queryset(self):
        cat = self.request.query_params.get('cat')
        if cat:
            return self.queryset.filter(categoriyasi__toifa=cat).all()
        return self.queryset.all()


class InstructorAPI(generics.CreateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

    def create(self, request, *args, **kwargs):
        data = dict()
        data['ism'] = request.data['ism']
        data['familiya'] = request.data['familiya']
        data['telefon'] = request.data['telefon']
        data['tuman'] = request.data['tuman']
        data['moshina'] = request.data['moshina']
        data['nomeri'] = request.data['nomeri']
        data['telegram_id'] = request.data['telegram_id']
        cat = request.data['toifa']
        obj = Category.objects.filter(toifa__exact=cat).first()
        data['toifa'] = [obj.id]
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        tel = serializer.validated_data['telegram_id']
        if Instructor.objects.filter(telegram_id=tel).first():
            return response.Response({'message': "ботимиздан аввал рўйхатдан ўтгансиз!",
                                      'message_ru': "Вы зарегистрировались раньше нашего бота!"})
        serializer.save()
        return response.Response(
            {'message': "ботимиздан рўйхатдан ўтдингиз!", 'message_ru': "Вы зарегистрировались с нашего бота!"})

    def get(self, request, *args, **kwargs):
        qs = self.queryset.filter(telegram_id=self.kwargs['pk'])
        serializer = self.get_serializer(instance=get_object_or_404(qs))
        return response.Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        qs = self.queryset.filter(telegram_id=self.kwargs['pk'])
        data = request.data
        cat = request.data.get('toifa', None)
        if cat:
            data = dict()
            obj = Category.objects.filter(toifa__exact=cat).first()
            data['toifa'] = [obj.id]
        serializer = self.get_serializer(instance=get_object_or_404(qs), data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)
