from django.db import models
from django.utils import timezone


class Promotion(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    # todo userselect > autoselect from link > default shop > default
    # todo img saving path would be unique for each entry
    image = models.ImageField(default='default.png', upload_to='promo_img', max_length=254, blank=True)
    shop = models.CharField(max_length=100) #todo linked to shop model or be "select or add" field
    active = models.BooleanField()
    online = models.BooleanField()
    weblink = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    startdate = models.DateTimeField(default=timezone.now)
    enddate = models.DateTimeField(blank=True, null=True) #todo if we reach end date active should change to false


    def __str__(self):
        return self.title



# Create your models here.

#TODO
#shop model - [name, type, link, image ]

