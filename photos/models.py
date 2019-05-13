from django.db import models
import datetime as dt  

# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length=30)
    
    def save_location(self):
        self.save()
        
    def delete_location(self):
        self.delete()
    
    def __str__(self):
        return self.location
    
class Category(models.Model):
    
    category = models.CharField(max_length =20)
    
    def save_category(self):
        self.save()
        
    def delete_category(self):
        self.delete()
    
    
    def __str__(self):
        return self.category


class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length =30)
    image_description = models.TextField(max_length=5000)
    date_taken = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
        
    @classmethod
    def search_by_category(cls,search_term):
        categories = cls.objects.filter(category__category__icontains=search_term)
        return categories
    
    @classmethod
    def get_image_by_id(cls, id):
        images = cls.objects.filter(location=location)
        return images
    
    @classmethod
    def filter_by_location(cls, location):
        images = cls.objects.filter(location=location)
        return images
    
    @classmethod
    def update_image(cls, id):
        images = cls.objects.filter(id=id).update(id=id)
        return images
    
    def __str__(self):
        return self.image_name
    

    
   
    
    
    

    
    
    
