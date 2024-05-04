from django.db import models

# Create your models here.

class Review(models.Model):
    full_name = models.CharField(max_length=20)
    user_review = models.TextField()
    movie = models.CharField(max_length=150, default="")
    
    
    def __str__(self):
        return self.full_name