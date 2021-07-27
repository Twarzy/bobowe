from rest_framework import serializers
from .models import Promotion

class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ['id', 'title', 'description', 'shop', 'active', 'online', 'weblink', 'date', 'startdate', 'enddate']
        #fields = '__all__'