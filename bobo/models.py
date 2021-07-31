from django.db import models
from django.utils import timezone



class Promotion(models.Model):

    CATEGORY = [
        ('INN', 'inna'),
        ('ZA', 'zabawki'),
        ('NEW', 'dla niemowlaka'),
        ('NAU', 'nauka'),
        ('PIE', 'pielęgnacja'),
        ('WIF', 'wózki i foteliki')
    ]

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    # todo userselect > autoselect from link > default shop > default
    # todo img saving path would be unique for each entry
    image = models.ImageField(default='default.jpg', upload_to='promo_img', max_length=254, blank=True)
    shop = models.CharField(max_length=100) #todo linked to shop model or be "select or add" field
    category = models.CharField(max_length=100, choices=CATEGORY, default='INN')
    active = models.BooleanField()
    highlight = models.BooleanField(default=False)
    online = models.BooleanField()
    weblink = models.URLField(max_length=200, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    startdate = models.DateTimeField(default=timezone.now)
    enddate = models.DateTimeField(blank=True, null=True) #todo if we reach end date active should change to false


    def __str__(self):
        return self.title



# Create your models here.

#TODO
#shop model - [name, type, link, image ]

