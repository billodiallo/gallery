from django.db import models
import datetime as dt

# Create your models here.
class Photographer(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    
    def __str__(self):
        return self.first_name
    def save_photographer(self):
        self.save()
    def delete_photographer(self):
        self.delete()

    @classmethod
    def display_photographers(cls):
        photographers= Photographer.objects.all()
        for photographer in photographers:
            return photographer        
    class Meta:
        ordering = ['first_name']


