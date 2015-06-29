from rest_framework import serializers
from time_management.models import Pooop


class PooopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pooop
        fields = ('id','start','end','duration')
