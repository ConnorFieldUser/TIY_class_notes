
from rest_framework import serializers

from menu_api.models import Special, Ingredient


class SpecialSerializer(serializers.ModelSerializer):
    ingredients = serializers.HyperlinkedRelatedField(
        many=True,
        view_name="ingredient_detail_update_destroy_api_view",
        read_only=True,
    )
    # created_by = serializers.ReadOnlyField()
    calorie_count = serializers.ReadOnlyField()
    my_favorite = serializers.SerializerMethodField()
    user = serializers.ReadOnlyField(source="created_by.id")

    def get_my_favorite(self, obj):
        return "PANCAKES!!!!"

    class Meta:
        model = Special
        exclude = ('created_by',)


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = '__all__'
