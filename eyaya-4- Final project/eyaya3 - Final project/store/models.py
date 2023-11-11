from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 



# Create your models here.
class Catergory(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    class meta:
        verbose_name_plural ='categories'

    def get_absolute_url(self):
        return reverse('store:category_list',args=[self.slug])

    def __str__(self):
        return self.name 
       
class Books(models.Model):
     catergory = models.ForeignKey(Catergory ,related_name='books',on_delete=models.CASCADE)
     created_by = models.ForeignKey(User ,on_delete=models.CASCADE,related_name='product_creator')
     title= models.CharField(max_length=255)
     author= models.CharField(max_length=255)
     isbn= models.CharField(max_length=255)
     copies= models.IntegerField(null=True)
     image = models.ImageField(upload_to='images/')
     slug = models.SlugField(max_length=255)
     in_stock =models.BooleanField(default=True)
     is_active =models.BooleanField(default=True)
     created = models.DateTimeField(auto_now_add= True)
     updated = models.DateTimeField(auto_now_add= True)

     class meta:
        verbose_name_plural ='books'
        ordering = ('-created')

     def get_absolute_url(self):
        return reverse('store:book',args=[str(self.slug)] )
    

     def __str__(self):
        return self.title
