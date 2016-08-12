import re
from django.core.urlresolvers import reverse
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)


class Vehicle(models.Model):
    type_of_vehicle = models.CharField(max_length=20)
    detail_of_vehicle = models.ImageField(upload_to=upload_location,
        null=True,
        blank=True,
        height_field="height_field",
        width_field="width_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    def __str__(self):
        return self.type_of_vehicle


class Location(models.Model):
    location = models.CharField(max_length= 20)
    def __str__(self):
        return self.location

def lnglat_validator(lnglat):
    if not re.match(r'^(\d+\.?\d*),(\d+\.?\d*)$', lnglat):
        raise forms.ValidationError('Invalid LngLat Type')



class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    vehicle = models.ForeignKey(Vehicle)
    price = models.IntegerField(help_text='30분 이용 가격')
    latlng = models.CharField(max_length=50, validators=[lnglat_validator], help_text='위도, 경도 포맷으로 입력', default='37.4624015, 126.9520365')
    location=models.ForeignKey(Location, default=1)
    # 캘린더 필드
    content = models.TextField()
    publish = models.DateField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def lat(self):
        return self.latlng.split(',')[0]

    def lng(self):
        return self.latlng.split(',')[1]

    def get_absolute_url(self):
        return reverse("blog:lend_detail", kwargs={"lend_id":self.id})

    def __str__(self):
        return self.title

class Rating(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL)
    ratings=models.DecimalField(max_digits=3, decimal_places=2, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    review=models.TextField()


class Date(models.Model):
    title = models.CharField(max_length=10)
    start = models.DateTimeField()
    end = models.DateTimeField()
    description = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.title
