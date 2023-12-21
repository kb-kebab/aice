from rest_framework import serializers

from .models import SaveOfferView


class SaveOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaveOfferView
        fields = '__all__'