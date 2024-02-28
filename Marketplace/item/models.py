from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Categorie(models.Model):
    name =  models.CharField(max_length=255)

    class Meta:
        #ordering =  ('name',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name


class Item(models.Model):
    categori= models.ForeignKey(Categorie, related_name='items', on_delete=models.CASCADE)
    name =  models.CharField(max_length=255)
    description = models.TextField(blank = True, null=True)
    prix = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    vendu = models.BooleanField(default=False)
    ajoute_par = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    ajoute_le = models.DateTimeField(auto_now_add=True)