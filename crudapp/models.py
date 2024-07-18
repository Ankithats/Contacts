from django.db import models

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=250)
    phone=models.CharField(max_length=15, blank=True, null=True)
    email=models.EmailField()
    alter=models.CharField(max_length=15, blank=True)
    image=models.ImageField(upload_to='todoimage', blank=True, null=True)
    
    def __str__(self):
        return self.name
    