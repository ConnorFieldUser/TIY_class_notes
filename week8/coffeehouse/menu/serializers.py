
from rest_framework import serializers

from menu.models import Special


class SpecialSerializer(serializers.ModelSerializer):

    image_url = serializers.ReadOnlyField()

    class Meta:
        model = Special
        fields = '__all__'
