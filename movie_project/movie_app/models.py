from django.db import models
from django.contrib.auth.models import User
from django.forms import SlugField
from django.urls import reverse
from django.utils.text import slugify

from autoslug import AutoSlugField

# Create your models here.

class  Category(models.Model):
    name=models.CharField(max_length=250)
   
    
    def get_absolute_url(self):
         return reverse('category_detail', kwargs={'pk': self.pk})
    
    

    def __str__(self):
        return self.name
    def get_movies(self):
         return Movie.objects.filter(category=self)

class Movie(models.Model):
    
    title = models.CharField(max_length=255, unique=True,null=True,blank=True)
    poster = models.ImageField(upload_to="posters/")  
    description = models.TextField()
    release_date = models.DateField()
    actors = models.CharField(max_length=255)  
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    trailer_link = models.URLField()  
    added_by = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
   

    class Meta:
         verbose_name_plural = "movies"
   
def __str__(self):
   return self.title   
def get_url(self):
        return reverse('detail', kwargs={'pk': self.pk}) 

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000, null=True)
    rating = models.FloatField(default=0)
def __str__(self):
        return self.user.username

    