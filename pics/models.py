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

    @classmethod
    def get_locations(cls):
        locations=cls.objects.all()
        return locations    
        
    class Meta:
        ordering=['location']

class Image(models.Model):
    # photo_image=CloudinaryField('photo_image')
    image = models.ImageField(upload_to = 'articles/',null = False)
    image_name = models.CharField(max_length=70)
    image_description = models.CharField(max_length=255)
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    location_id = models.ForeignKey(Location,on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()  

    @classmethod
    def update_image(cls,id,value):
        image = cls.objects.filter(id=id).update(photo_image=value)
    
    @classmethod
    def get_image_by_id(cls,id):
        image=cls.objects.filter(id=id).all()
        return image 

    @classmethod
    def get_image_by_location(cls,location):
        location=Image.objects.filter(location_id_id=location).all()
        return location
    
    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(category_id__category__icontains=search_term)
        return images
    
    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images
    
    class Meta:
        ordering=['date_posted'] 
