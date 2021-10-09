from django.test import TestCase
from .models import Location,Category,Image

#creating your tests here
class CategoryTestClass(TestCase):
    def setUp(self):
        self.caleb = Category(category='Place')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.caleb,Category))   
        
    def test_save_method(self):
        self.caleb.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)     
        
class LocationTestClass(TestCase):
    def setUp(self):
        self.kimt = Location(location='Nakuru')     
        
    def test_instance(self):
        self.assertTrue(isinstance(self.kimt,Location))
        
    def test_save_method(self):
        self.kimt.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)        
        
class ImageTestClass(TestCase):
    def setUp(self):
        self.location = Location(location='Nakuru')
        self.location.save_location()

        self.category = Category(category='love')
        self.category.save_category()
        
        self.latif = Image(id=1,photo_image='yes.jpg',image_name='test',image_description='test image',location_id=self.location,category_id=self.category,date_posted='2021-06-06')   
        
    def test_instance(self):
        self.assertTrue(isinstance(self.latif,Image))        
        
    def test_save_method(self):
        self.latif.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)    
        
    def test_delete_image(self):
        self.latif.delete_image()
        image = Image.objects.all()
        self.assertTrue(len(image)==0)       
        
    def test_update_image(self):
        self.latif.save_image()
        self.latif.update_image(self.latif.id,'photos/me.png')    
        image = Image.objects.filter(photo_image='photos/me.png')
        self.assertTrue(len(image)>0)  
        
    def test_get_image_by_id(self):
        image_k=self.latif.get_image_by_id(self.latif.id)
        image=Image.objects.filter(id=self.latif.id)    
        self.assertTrue(image_k.query,image.query)
        
    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete() 
        Category.objects.all().delete()   
