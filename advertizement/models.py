from django.db import models
from django.core.exceptions import ValidationError
from PIL import Image
from django.core.files.base import ContentFile
from io import BytesIO


class AdvertizementFirst(models.Model):
    advertizement_first_image = models.ImageField(upload_to='images/advertizements', blank=True, null=True)
    advertizement_first_url = models.URLField(default='#')

    def save(self, *args, **kwargs):
        try:
            # is the object in the database yet?
            this = AdvertizementFirst.objects.get(id=self.id)
            if this.advertizement_first_image != self.advertizement_first_image:
                this.advertizement_first_image.delete(save=False)
        except: pass # when new photo then we do nothing, normal case

        if not self.pk and AdvertizementFirst.objects.exists():
            raise ValidationError('There is can be only one Advertizement First instance')

        # Optimize image before saving
        if self.advertizement_first_image:
            img = Image.open(self.advertizement_first_image)
            output = BytesIO()

            # Save the image in its original format
            img_format = img.format
            img.save(output, format=img_format, quality=75)
            output.seek(0)
            self.advertizement_first_image = ContentFile(output.read(), self.advertizement_first_image.name)

        return super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        self.advertizement_first_image.delete(save=False)
        super().delete(*args, **kwargs)

# Similar changes can be made to AdvertizementSecond and Favicon models
class AdvertizementSecond(models.Model):
    advertizement_second_image = models.ImageField(upload_to='images/advertizements', blank=True, null=True)
    advertizement_second_url = models.URLField(default='#')
   
    def save(self, *args, **kwargs):
        try:
            # is the object in the database yet?
            this = AdvertizementSecond.objects.get(id=self.id)
            if this.advertizement_second_image != self.advertizement_second_image:
                this.advertizement_second_image.delete(save=False)
        except: pass # when new photo then we do nothing, normal case

        if not self.pk and AdvertizementSecond.objects.exists():
            raise ValidationError('There is can be only one Advertizement Second instance')

        # Optimize image before saving
        if self.advertizement_second_image:
            img = Image.open(self.advertizement_second_image)
            output = BytesIO()

            # Save the image in its original format
            img_format = img.format
            img.save(output, format=img_format, quality=75)
            output.seek(0)
            self.advertizement_second_image = ContentFile(output.read(), self.advertizement_second_image.name)

        return super().save(*args, **kwargs)
    def delete(self, *args, **kwargs):
        self.advertizement_second_image.delete(save=False)
        super().delete(*args, **kwargs)


class AdvertizementThird(models.Model):
    advertizement_third_image = models.ImageField(upload_to='images/advertizements', blank=True, null=True)
    advertizement_third_url = models.URLField(default='#')
   
    def save(self, *args, **kwargs):
        try:
            # is the object in the database yet?
            this = AdvertizementThird.objects.get(id=self.id)
            if this.advertizement_third_image != self.advertizement_third_image:
                this.advertizement_third_image.delete(save=False)
        except: pass # when new photo then we do nothing, normal case

        if not self.pk and AdvertizementThird.objects.exists():
            raise ValidationError('There is can be only one Advertizement Third instance')

        # Optimize image before saving
        if self.advertizement_third_image:
            img = Image.open(self.advertizement_third_image)
            output = BytesIO()

            # Save the image in its original format
            img_format = img.format
            img.save(output, format=img_format, quality=75)
            output.seek(0)
            self.advertizement_third_image = ContentFile(output.read(), self.advertizement_third_image.name)

        return super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        self.advertizement_third_image.delete(save=False)
        super().delete(*args, **kwargs)

class Favicon(models.Model):
    favicon_image = models.ImageField(upload_to='images/advertizements', blank=True, null=True)
   
    def save(self, *args, **kwargs):
        try:
            # is the object in the database yet?
            this = Favicon.objects.get(id=self.id)
            if this.favicon_image != self.favicon_image:
                this.favicon_image.delete(save=False)
        except: pass # when new photo then we do nothing, normal case

        if not self.pk and Favicon.objects.exists():
            raise ValidationError('There is can be only one Favicon instance')

        # Optimize image before saving
        if self.favicon_image:
            img = Image.open(self.favicon_image)
            output = BytesIO()

            # Save the image in its original format
            img_format = img.format
            img.save(output, format=img_format, quality=75)
            output.seek(0)
            self.favicon_image = ContentFile(output.read(), self.favicon_image.name)

        return super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        self.favicon_image.delete(save=False)
        super().delete(*args, **kwargs)