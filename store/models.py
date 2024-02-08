# models.py
from django.db import models
from django.urls import reverse
from category.models import Category
from users.models import CustomUser
# from django.db.models import Count, F, Manager

class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(variation_category='color', is_active=True)

    def sizes(self):
        return super(VariationManager, self).filter(variation_category='size', is_active=True)

class Color(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# class ProductManager(Manager):
#     def most_liked(self):
#         return self.annotate(likes_count=Count('likes')).order_by('-likes_count')

class Product(models.Model):
    product_name = models.CharField(max_length=150, unique=True)
    product_brand = models.CharField(max_length=150, blank=True,default='Unknown Brand')
    product_slug = models.SlugField(max_length=150, unique=True)
    product_description = models.TextField(blank=True, null=True)
    product_price = models.IntegerField()
    product_stock = models.IntegerField()
    product_is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_created_date = models.DateTimeField(auto_now_add=True)
    product_modified_date = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(CustomUser, through="Like", related_name="liked_products")
    product_views_count = models.PositiveIntegerField(default=0)
    product_phone = models.CharField(max_length=15, blank=True, null=True)
    product_owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='owned_products', default=1)
    
    # objects = ProductManager()
    
    def increment_views(self):
        self.product_views_count += 1
        self.save()
        
    def get_store_url(self):
        if self.category and self.category.category_slug and self.product_slug:
            return reverse('product_detail', args=[self.category.category_slug, self.product_slug])
        else:
            return "#"

    def get_main_image(self):
        main_images = [image for image in self.images.all() if image.is_main]
        return main_images[0] if main_images else None
    
    def likes_count(self):
        return self.likes.count()

    def __str__(self):
        return self.product_name
    

class Like(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_likes")
    liked_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

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

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'

    def __str__(self):
        return self.product.product_name + " Image"
    
    def save(self, *args, **kwargs):
        if self.is_main:
            ProductImage.objects.filter(product=self.product, is_main=True).update(is_main=False)
        super().save(*args, **kwargs)

class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variations')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, blank=True, null=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now=True)

    objects = VariationManager()

    def __str__(self):
        return f"{self.product.product_name} - {self.color} - {self.size} - {self.is_active}"


