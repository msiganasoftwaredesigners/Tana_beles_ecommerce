# models.py
from django.db import models
from django.urls import reverse
from category.models import Category
from django.core.exceptions import ValidationError

from PIL import Image  
from django.core.files.base import ContentFile
from io import BytesIO 
import os
# from django.db.models import Count, F, Manager

class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(variation_category='color', is_active=True)

    def sizes(self):
        return super(VariationManager, self).filter(variation_category='size', is_active=True)


class Size(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Color(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    product_name = models.CharField(max_length=150, unique=True)
    product_brand = models.CharField(max_length=150, blank=True,default='Custom')
    product_slug = models.SlugField(max_length=150, unique=True)
    product_description = models.TextField(blank=True, null=True)
    product_stock = models.IntegerField()
    product_is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_created_date = models.DateTimeField(auto_now_add=True)
    product_modified_date = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField('users.CustomUser', through="Like", related_name="liked_products")
    product_views_count = models.PositiveIntegerField(default=0)
    product_phone = models.CharField(max_length=15, blank=True, null=True)
    product_owner = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='owned_products', default=1)
     
    @property
    def default_price(self):
        size_variations = SizeVariation.objects.filter(product=self).order_by('id')
        if size_variations.exists():
            return size_variations.first().price
        else:
            return None
    
    def increment_views(self):
        print("increment_views was called on product with slug:", self.product_slug)
        self.product_views_count += 1
        self.save()
        print("product_views_count after incrementing:", self.product_views_count)
    
    def save(self, *args, **kwargs):
        print("Product is being saved. Current views count is", self.product_views_count)
        super().save(*args, **kwargs)

    def validate_unique(self, exclude=None):
        super().validate_unique(exclude)
        if Product.objects.filter(product_name=self.product_name).exclude(id=self.id).exists():
            raise ValidationError({'product_name': ('Product with this name already exists.')})
        
    def get_store_url(self):
        if self.category and self.category.category_slug and self.product_slug:
            return reverse('product_detail', args=[self.category.category_slug, self.product_slug])
        else:
            return "#"

    def get_short_name(self):
        return self.product_name[:16]
    # def get_main_image(self):
    #     main_images = [image for image in self.images.all() if image.is_main]
    #     return main_images[0] if main_images else None
    def get_main_image(self):
        main_image = self.images.filter(is_main=True).first()
        return main_image
    
    
    def likes_count(self):
        return self.likes.count()

    def __str__(self):
        return self.product_name
    

class Like(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_likes")
    liked_by = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.
        self.product.product_likes_count = self.product.product_likes.count()
        self.product.save()

    def delete(self, *args, **kwargs):
        product = self.product
        super().delete(*args, **kwargs)  # Call the "real" delete() method.
        product.product_likes_count = product.product_likes.count()
        product.save()

    def __str__(self):
        return f"{self.liked_by} liked {self.product.product_name}"

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/images')
    is_main = models.BooleanField(default=False)
    
    def clean(self):
        super().clean()
        if self.image:
            if self.image.size > 2*1024 * 1024:  # 2MB
                raise ValidationError({'image': ('Image file too large ( > 750mb )')})

    def save(self, *args, **kwargs):
        try:
           # is the object in the database yet?
           this = ProductImage.objects.get(id=self.id)
           if this.image != self.image:
               this.image.delete(save=False)
        except: pass # when new photo then we do nothing, normal case

        # Optimize image before saving
        if self.image:
           img = Image.open(self.image)
           output = BytesIO()
  
           # Save the image in its original format
           img_format = self.image.name.split('.')[-1]  # Get the file extension
           img.save(output, format=img_format, quality=75)
           output.seek(0)
           self.image = ContentFile(output.read(), self.image.name)

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
    # Delete the actual image file
        try:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        except PermissionError:
            print("Permission denied: Unable to delete the image file.")
        except Exception as e:
            print(f"Unexpected error occurred while deleting the image file: {e}")
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'

    def __str__(self):
        return self.product.product_name + " Image"
    

class SizeVariation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)

class Variation(models.Model):
    size_variation = models.ForeignKey(SizeVariation, on_delete=models.CASCADE)
    color = models.ManyToManyField(Color, blank=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now=True)
    objects = VariationManager()

    def __str__(self):
        return f"{self.size_variation.product.product_name} - {', '.join([color.name for color in self.color.all()])} - {self.size_variation.size} - {self.size_variation.price} - {self.is_active}"