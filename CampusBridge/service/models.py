from django.db import models
from django.contrib.auth.models import User

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
    start_price = models.DecimalField(max_digits=10, decimal_places=2)
    end_price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    
    class Meta:
        ordering = ('-created',)
        
    def __str__(self):
        return self.name


    def get_display_StartPrice(self):
        return self.start_price
    
    def get_display_EndPrice(self):
        return self.end_price
    
    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                
                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x240x.jpg'