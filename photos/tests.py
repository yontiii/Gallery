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