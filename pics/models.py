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
