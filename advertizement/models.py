from django.db import models
from django.core.exceptions import ValidationError
from PIL import Image
from django.core.files.base import ContentFile
from io import BytesIO
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver


class AdvertizementFirst(models.Model):
    advertizement_first_image = models.ImageField(upload_to='images/advertizements', blank=True, null=True)
    advertizement_first_url = models.URLField(blank=True)

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
            if img.format != 'GIF':
                output = BytesIO()

                # Save the image in its original format
                img_format = img.format
                img.save(output, format=img_format, quality=75)
                output.seek(0)
                self.advertizement_first_image = ContentFile(output.read(), self.advertizement_first_image.name)

        return super().save(*args, **kwargs)
    def delete(self, *args, **kwargs):
    # Delete the actual image file
        try:
            self.advertizement_first_image.delete(save=False)
        except PermissionError:
            print("Permission denied: Unable to delete the image file.")
        except Exception as e:
            print(f"Unexpected error occurred while deleting the image file: {e}")
        super().delete(*args, **kwargs)
    
@receiver(post_delete, sender=AdvertizementFirst)
def delete_advertizement_first_image(sender, instance, **kwargs):
    """Delete the actual image file when an AdvertizementFirst object is deleted."""
    instance.advertizement_first_image.delete(save=False)

@receiver(pre_save, sender=AdvertizementFirst)
def delete_old_image_on_update(sender, instance, **kwargs):
    """Delete the old image file when an AdvertizementFirst object is updated."""
    if instance.pk:
        old_image = AdvertizementFirst.objects.get(pk=instance.pk).advertizement_first_image
        new_image = instance.advertizement_first_image
        if old_image and new_image and old_image != new_image:
            old_image.delete(save=False)


class AdvertizementSecond(models.Model):
    advertizement_second_image = models.ImageField(upload_to='images/advertizements', blank=True, null=True)
    advertizement_second_url = models.URLField(blank=True)
   
    def save(self, *args, **kwargs):
        try:
            this = AdvertizementSecond.objects.get(id=self.id)
            if this.advertizement_second_image != self.advertizement_second_image:
                this.advertizement_second_image.delete(save=False)
        except: pass 

        if not self.pk and AdvertizementSecond.objects.exists():
            raise ValidationError('There is can be only one Advertizement Second instance')

        if self.advertizement_second_image:
            img = Image.open(self.advertizement_second_image)
            if img.format != 'GIF':
                output = BytesIO()

                img_format = img.format
                img.save(output, format=img_format, quality=75)
                output.seek(0)
                self.advertizement_second_image = ContentFile(output.read(), self.advertizement_second_image.name)

        return super().save(*args, **kwargs)
    def delete(self, *args, **kwargs):
        self.advertizement_second_image.delete(save=False)
        super().delete(*args, **kwargs)

@receiver(post_delete, sender=AdvertizementSecond)
def delete_advertizement_second_image(sender, instance, **kwargs):
    """Delete the actual image file when an AdvertizementSecond object is deleted."""
    instance.advertizement_second_image.delete(save=False)

@receiver(pre_save, sender=AdvertizementSecond)
def delete_old_image_on_update(sender, instance, **kwargs):
    """Delete the old image file when an AdvertizementSecond object is updated."""
    if instance.pk:
        old_image = AdvertizementSecond.objects.get(pk=instance.pk).advertizement_second_image
        new_image = instance.advertizement_second_image
        if old_image and new_image and old_image != new_image:
            old_image.delete(save=False)


class AdvertizementThird(models.Model):
    advertizement_third_image = models.ImageField(upload_to='images/advertizements', blank=True, null=True)
    advertizement_third_url = models.URLField(blank=True)
   
    def save(self, *args, **kwargs):
        try:
            this = AdvertizementThird.objects.get(id=self.id)
            if this.advertizement_third_image != self.advertizement_third_image:
                this.advertizement_third_image.delete(save=False)
        except: pass 

        if not self.pk and AdvertizementThird.objects.exists():
            raise ValidationError('There is can be only one Advertizement Third instance')

        if self.advertizement_third_image:
            img = Image.open(self.advertizement_third_image)
            if img.format != 'GIF':
                output = BytesIO()

                img_format = img.format
                img.save(output, format=img_format, quality=75)
                output.seek(0)
                self.advertizement_third_image = ContentFile(output.read(), self.advertizement_third_image.name)

        return super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        self.advertizement_third_image.delete(save=False)
        super().delete(*args, **kwargs)

@receiver(post_delete, sender=AdvertizementThird)
def delete_advertizement_third_image(sender, instance, **kwargs):
    """Delete the actual image file when an AdvertizementThird object is deleted."""
    instance.advertizement_third_image.delete(save=False)

@receiver(pre_save, sender=AdvertizementThird)
def delete_old_image_on_update(sender, instance, **kwargs):
    """Delete the old image file when an AdvertizementThird object is updated."""
    if instance.pk:
        old_image = AdvertizementThird.objects.get(pk=instance.pk).advertizement_third_image
        new_image = instance.advertizement_third_image
        if old_image and new_image and old_image != new_image:
            old_image.delete(save=False)


class Favicon(models.Model):
    favicon_image = models.ImageField(upload_to='images/favicon', blank=True, null=True)
   
    def save(self, *args, **kwargs):
        try:
            this = Favicon.objects.get(id=self.id)
            if this.favicon_image != self.favicon_image:
                this.favicon_image.delete(save=False)
        except: pass 

        if not self.pk and Favicon.objects.exists():
            raise ValidationError('There is can be only one Favicon instance')
       
        if self.favicon_image:
            img = Image.open(self.favicon_image)
            output = BytesIO()

          
            img_format = img.format
            img.save(output, format=img_format, quality=75)
            output.seek(0)
            self.favicon_image = ContentFile(output.read(), self.favicon_image.name)

        return super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        self.favicon_image.delete(save=False)
        super().delete(*args, **kwargs)

@receiver(post_delete, sender=Favicon)
def delete_favicon_image(sender, instance, **kwargs):
    """Delete the actual image file when an Favicon object is deleted."""
    instance.favicon_image.delete(save=False)

@receiver(pre_save, sender=Favicon)
def delete_old_image_on_update(sender, instance, **kwargs):
    """Delete the old image file when an Favicon object is updated."""
    if instance.pk:
        old_image = Favicon.objects.get(pk=instance.pk).favicon_image
        new_image = instance.favicon_image
        if old_image and new_image and old_image != new_image:
            old_image.delete(save=False)