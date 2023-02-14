from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.

CATEGORY_CHOICES=(
    ('M','Mobile'),
    ('TW','Top Wear'),
    ('BW','Bottom Wear'),
)
class Product(models.Model):
    title=models.CharField(max_length=100)
    price=models.FloatField()
    description=models.TextField()
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_iamge=models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)


