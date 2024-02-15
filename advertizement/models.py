from django.db import models
from django.core.exceptions import ValidationError

class AdvertizementFirst(models.Model):
    advertizement_first_image = models.ImageField(upload_to='images/advertizements', blank=True, null=True)
    advertizement_first_url = models.URLField()
    def save(self, *args, **kwargs):
        if not self.pk and AdvertizementFirst.objects.exists():
            raise ValidationError('There is can be only one Advertizement First instance')
        return super(AdvertizementFirst, self).save(*args, **kwargs)
    
class AdvertizementSecond(models.Model):
    advertizement_second_image = models.ImageField(upload_to='images/advertizements', blank=True, null=True)
    advertizement_second_url = models.URLField()
    def save(self, *args, **kwargs):
        if not self.pk and AdvertizementSecond.objects.exists():
            raise ValidationError('There is can be only one Advertizement Second instance')
        return super(AdvertizementSecond, self).save(*args, **kwargs)
    
class AdvertizementThird(models.Model):
    advertizement_third_image = models.ImageField(upload_to='images/advertizements', blank=True, null=True)
    advertizement_third_url = models.URLField()
    def save(self, *args, **kwargs):
        if not self.pk and AdvertizementThird.objects.exists():
            raise ValidationError('There is can be only one Advertizement Third instance')
        return super(AdvertizementThird, self).save(*args, **kwargs)
    