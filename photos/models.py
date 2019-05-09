from django.db import models
import datetime as dt  

# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length=30)
    
    def __str__(self):
        return self.location

class Category(models.Model):
    
    category = models.CharField(max_length =20)
    
    def __str__(self):
        return self.category


class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length =30)
    image_description = models.TextField(max_length=50)
    date_taken = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
    
    def __str__(self):
        return self.image_name
    
   
    
    
    

    
    
    
