from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from pooopers.models import Poooper
from pooopers.serializers import PoooperSerializer
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework import status



class PoooperViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Poooper.objects.all()
    serializer_class = PoooperSerializer

    @detail_route(methods=['post','get'],url_path='reset')
    def reset(self,request,pk=None):
        user = self.get_object()
        user.pooops.all().delete()
        return Response(None,status=status.HTTP_204_NO_CONTENT)

