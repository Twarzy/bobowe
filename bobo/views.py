from django.shortcuts import render
from rest_framework import viewsets
from .models import Promotion
from .serializers import PromotionSerializer
from django.views.generic import ListView, DetailView, CreateView, UpdateView

class MainView(ListView):
    model = Promotion
    template_name = 'bobo/home.html'
    context_object_name = 'promotions'
    paginate_by = 2 #Will be expand to 10

    def get_queryset(self):
        return Promotion.objects.all()

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Promotion._meta.fields]

class PromotionDetailView(DetailView):
    model = Promotion



#API viewset
class PromotionViewSet(viewsets.ModelViewSet):
    serializer_class = PromotionSerializer
    queryset = Promotion.objects.all()




