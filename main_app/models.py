from django.db import models
from django.urls import reverse
# Create your models here.

class Widget(models.Model):
    description = models.TextField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return self.description
        
    def get_absolute_url(self):
        return reverse('home', kwargs={'widget_id': self.id})