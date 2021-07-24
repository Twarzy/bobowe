from django.shortcuts import render
from rest_framework import viewsets
from .models import Promotion
from .serializers import PromotionSerializer

class PromotionViewSet(viewsets.ModelViewSet):
    serializer_class = PromotionSerializer
    queryset = Promotion.objects.all()


# Create your views here.
