from django.db import models
# from cloudinary.models import CloudinaryField

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=100)
    
    def __str__(self):
        return self.category
    
    def save_category(self):
        self.save()
        
    class Meta:
        ordering=['category']

class Location(models.Model):
    location= models.CharField(max_length=100)
    
    def __str__(self):
        return self.location
    
    def save_location(self):
        self.save()
