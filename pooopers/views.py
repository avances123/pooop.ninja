from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from pooopers.models import Poooper
from pooopers.serializers import PoooperSerializer


class PoooperViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Poooper.objects.all()
    serializer_class = PoooperSerializer
