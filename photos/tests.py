from django.test import TestCase
from .models import Image,Location,Category

# Create your tests here.

class ImageTestClass(TestCase):
    
    # Setup method
    def setUp(self):
        self.location = Location(location='Africa')
        self.location.save()
        
        self.category = Category(category = 'fun')
        self.category.save()
        
        self.image = Image(image = 'image1.jpg', image_name='test',image_description='This is a test image',date_taken='2017-2-28',location = self.location, category = self.category)
        
        
    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()
        
        
        
    # Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))
        
    # testing the save method
    def test_save_method(self):
        self.image = Image(image = 'image1.jpg', image_name='test',image_description='This is a test image',date_taken='2017-2-28',location = self.location, category = self.category)
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) >= 1)
        
    def test_delete_method(self):
        self.image = Image(image = 'image1.jpg', image_name='test',image_description='This is a test image',date_taken='2017-2-28',location = self.location, category = self.category)
        self.image.save_image()
        images = self.image.delete_image()
        deleted = Image.objects.all()
        self.assertTrue(len(deleted) <= 0)
        
    def test_update_method(self):
        
        
        
class LocationTestClass(TestCase):
    # SetUp Class
    def setUp(self):
        self.location = Location(location="Nairobi")
        
    def tearDown(self):
        Location.objects.all().delete()
        
    def test_save_location(self):
        self.location.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location)>= 1)
        
    def test_delete_location(self):
        self.location.save_location()
        locations = self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) <= 0)
        
class CategoryTestClass(TestCase):
     # SetUp Class
    def setUp(self):
        self.category = Category(category="Fun")
        
    def tearDown(self):
        Category.objects.all().delete()
        
    def test_save_category(self):
        self.category.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category)>= 1)
        
    def test_delete_category(self):
        self.category.save_category()
        categories = self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) <= 0)
    
        
        
        