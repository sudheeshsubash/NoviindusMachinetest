from django.db import models

# Create your models here.

from django.contrib.auth.models import User



class ShortCourse(models.Model):
    
    status_choice = (
        ('Enable', 'enable'),
        ('Disable', 'disable'),   
    )
    image = models.ImageField(upload_to='image')
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    discription = models.TextField()
    status = models.CharField(max_length=255, choices=status_choice)
    amount = models.IntegerField()
    createdat = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.title