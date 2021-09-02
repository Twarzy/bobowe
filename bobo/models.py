from django.db import models
from django.utils import timezone


class Promotion(models.Model):

    CATEGORY = [
        ('INN', 'inne'),
        ('ZAB', 'zabawki'),
        ('NEW', 'dla niemowlaka'),
        ('NAU', 'nauka'),
        ('PIE', 'pielęgnacja'),
        ('WIF', 'wózki i foteliki')
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    price = models.FloatField(blank=True, null=True)
    old_price = models.FloatField(blank=True, null=True)
    # todo userselect > autoselect from link > default shop > default
    # todo img saving path would be unique for each entry
    # todo create image also different file as thumbnail
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
    #todo if enddate is close to now there should be somekind of notification

    @property
    def discount(self):
        discount = round(((self.old_price - self.price) / self.old_price * 100), 2)
        return discount

    def __str__(self):
        return self.title

#TODO auto generate and add affilate part of link for ex. allegro.pl
#TODO use bitly api, for automatic shorten link, and get click report for link



class Diaper(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    size = models.CharField(max_length=100, blank=True)
    online = models.BooleanField()
    weblink = models.URLField(blank=True)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()

    @property
    def price_pp(self):  #price per piece
        ppp = int(self.price / self.quantity * 100)
        return ppp


    def __str__(self):
        if self.size:
            return self.brand + ' ' + self.name + ' ' + self.size
        else:
            return self.brand + ' ' + self.name

    #image



# Create your models here.

#TODO
#shop model - [name, type, link, image ]

