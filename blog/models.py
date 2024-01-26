from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/posts', blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    short_description = models.CharField(max_length=200, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if self.content:
            # Set the short_description as the first 200 characters of the content
            self.short_description = self.content[:150]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title