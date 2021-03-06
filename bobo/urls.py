"""bobowe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import PromotionViewSet, MainView, PromotionDetailView, DiaperListView,CategoryListView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('promotions', PromotionViewSet, basename='promotions')

urlpatterns = [
    path('api/', include(router.urls)),
    path('', MainView.as_view(), name='home'),
    path('okazje/<int:pk>/', PromotionDetailView.as_view(), name='okazja'),
    path('pieluchy/', DiaperListView.as_view(), name='pieluchy'),
    path('kategoria/', CategoryListView.as_view(), name='kategoria')
    #path('viewset/<int:pk>/', include(router.urls)),
]
