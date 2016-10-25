
from rest_framework import serializers

from menu_api.models import Special


class SpecialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Special
        fields = '__all__'
