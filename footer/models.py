from django.db import models
from django.core.exceptions import ValidationError

class Footer(models.Model):
    phone_number = models.CharField(max_length=15)
    company_logo = models.ImageField(upload_to='images/contacts', blank=True)
    email = models.EmailField(max_length=50, blank=True)
    company_description = models.TextField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk and Footer.objects.exists():
            raise ValidationError('There is can be only one Footer instance')
        return super(Footer, self).save(*args, **kwargs)