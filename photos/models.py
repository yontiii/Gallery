from django.db import models

# Create your models here.
class Image(models.Model):
    image_name = models.CharField(max_length =30)
    image_description = models.TextField(max_length=50)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    date_taken = mo
    
    def __str__(self):
        return self.image_name

class Location(models.Model:

    
    
    
