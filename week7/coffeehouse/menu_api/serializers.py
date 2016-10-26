
from rest_framework import serializers

from menu_api.models import Special, Ingredient


class SpecialSerializer(serializers.ModelSerializer):
    ingredients = serializers.HyperlinkedRelatedField(
        many=True,
        view_name="ingredient_detail_update_destroy_api_view",
        read_only=True,
    )
    calorie_count = serializers.IntegerField()
    my_favorite = serializers.SerializerMethodField()

    def get_my_favorite(self, obj):
        return "PANCAKES!!!!"

    class Meta:
        model = Special
        fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = '__all__'
