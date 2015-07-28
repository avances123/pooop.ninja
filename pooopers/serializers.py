from rest_framework import serializers
from pooopers.models import Poooper


class PoooperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Poooper
        fields = ('username', 'email','total_poooped','salary','total_earned')
