from django.contrib import admin
from. models import Product
# Register your models here.

admin.site.register(Product)
class ProdcutModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','price','description','category','product_image']

