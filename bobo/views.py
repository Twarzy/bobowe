from django.shortcuts import render
from django.db.models import Q
from rest_framework import viewsets
from .models import Promotion, Diaper
from .serializers import PromotionSerializer
from django.views.generic import ListView, DetailView, CreateView, UpdateView
import random
import string

class MainView(ListView):
    model = Promotion
    template_name = 'bobo/home.html'
    context_object_name = 'promotions'
    paginate_by = 5 #Will be expand to 10
    ordering = ['-date']

    #Search field from navbar modify queryset
    def get_queryset(self):
        if self.request.GET.get('search'):
            search_field = self.request.GET.get('search') if self.request.GET.get('search') else '123'
            return Promotion.objects.filter(Q(title__icontains=search_field) |
                                            Q(shop__icontains=search_field)
            ).order_by('-date')
        else:
            return Promotion.objects.all().order_by('-date')


class PromotionDetailView(DetailView):
    model = Promotion


class DiaperListView(ListView):
    model = Diaper
    template_name = 'bobo/diapers.html'
    context_object_name = 'diapers'

class CategoryListView(ListView):
    model = Promotion
    template_name = 'bobo/category.html'
    context_object_name = 'promotions'
    #TODO paginate not working with geting url parameter
    paginate_by = 5 #Will be expand to 10

    category_list = model.CATEGORY

    def get_queryset(self):
        return Promotion.objects.filter(category=self.request.GET.get('category')).order_by('-date')


#API viewset
class PromotionViewSet(viewsets.ModelViewSet):
    serializer_class = PromotionSerializer
    queryset = Promotion.objects.all().order_by('-date')


# Create Promotion obj for testing

def promotion_add(number):

    category = ['INN', 'ZAB', 'NEW', 'NAU', 'PIE', 'WIF']
    shop_list = ['biedronka', 'sizeer', 'allegro', 'al.to', 'osiedlowy', 'mięsny', 'dino']


    for x in range(number):

        obj = Promotion.objects.create(
            title='Promocja Testowa {}'.format(x),
            description=''.join(random.choices(string.ascii_uppercase + string.digits, k=100)),
            shop=random.choice(shop_list),
            category=random.choice(category),
            active=random.choice(['True', 'False']),
            online=random.choice(['True', 'False'])
        )
        obj.save()




