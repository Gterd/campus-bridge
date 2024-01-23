from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    
    class Meta:
        ordering = ('name',)
        
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    
    class Meta:
        ordering = ('-created',)
        
    def __str__(self):
        return self.name


    def get_display_price(self):
        return self.price
    
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