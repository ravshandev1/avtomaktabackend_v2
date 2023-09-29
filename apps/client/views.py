from rest_framework import generics, response, status, views
from .models import Information
from .serializers import InformationSerializer
from instructor.models import Instructor


class InformationAPI(generics.RetrieveAPIView):
    queryset = Information
    serializer_class = InformationSerializer


class DeleteUserAPI(views.APIView):
    def get_queryset(self):
        instructor = Instructor.objects.filter(telegram_id=self.kwargs['pk']).first()
        return instructor

    def delete(self, request, *args, **kwargs):
        obj = self.get_queryset()
        obj.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)
