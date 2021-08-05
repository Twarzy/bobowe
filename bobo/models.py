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


    def __str__(self):
        return self.title

class Diaper(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    size = models.CharField(max_length=100, blank=True)
    online = models.BooleanField()
    weblink = models.URLField(blank=True)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()

    #price per piece
    @property
    def ppp(self):
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

