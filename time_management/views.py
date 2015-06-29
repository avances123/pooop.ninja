from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from time_management.models import Pooop
from time_management.serializers import PooopSerializer



class PooopViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Pooop.objects.all()
    serializer_class = PooopSerializer
