from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from sorl.thumbnail import ImageField, get_thumbnail

class College(models.Model):
    school_name = models.CharField(max_length=255)

    class Meta:
        ordering = ('school_name',)
        
    def __str__(self):
        return self.school_name


class Service_Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    
    class Meta:
        ordering = ('name',)
        
    def __str__(self):
        return self.name

class Service(models.Model):
    school_available = models.ForeignKey(College, on_delete=models.CASCADE)
    provider = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Service_Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = ImageField(upload_to='uploads/', blank=True, null=True)
    
    class Meta:
        ordering = ('-created',)
        
    def __str__(self):
        return self.name


    def get_display_price(self):
        return self.price

    def display_thumbnail(self):
        return self.thumbnail.url
    
    def save(self, *args, **kwargs):
        
        if self.thumbnail:
            self.thumbnail = get_thumbnail(self.thumbnail, '500x600', quality=99, format='JPEG').url

        if self.image:
            self.image = get_thumbnail(self.image, '500x600', quality=99, format='JPEG').url
        super(Service, self).save(*args, **kwargs)