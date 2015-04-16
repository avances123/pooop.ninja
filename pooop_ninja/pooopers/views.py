from rest_framework import viewsets
from pooop_ninja.pooopers.models import Poooper
from pooop_ninja.pooopers.serializers import PoooperSerializer


class PoooperViewSet(viewsets.ModelViewSet):
    queryset = Poooper.objects.all()
    serializer_class = PoooperSerializer