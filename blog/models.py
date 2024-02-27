from django.db import models
from django.utils.text import slugify
from PIL import Image
from django.core.files.base import ContentFile
from io import BytesIO

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='images/posts', blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    short_description = models.CharField(max_length=200, blank=True)

    def save(self, *args, **kwargs):
        try:
            # is the object in the database yet?
            this = Post.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except: pass # when new photo then we do nothing, normal case

        self.slug = slugify(self.title)
        if self.content:
            # Set the short_description as the first 200 characters of the content
            self.short_description = self.content[:150]

        # Optimize image before saving
        if self.image:
            img = Image.open(self.image)
            output = BytesIO()

            # Save the image in its original format
            img_format = img.format
            img.save(output, format=img_format, quality=75)
            output.seek(0)
            self.image = ContentFile(output.read(), self.image.name)

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title