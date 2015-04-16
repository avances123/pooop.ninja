from rest_framework import serializers
from pooop_ninja.pooopers.models import Poooper


class PoooperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Poooper
        fields = ('username', 'email', 'is_staff')
