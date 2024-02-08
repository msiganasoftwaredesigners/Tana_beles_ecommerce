from django.db import models
from django.core.exceptions import ValidationError

class Footer(models.Model):
    nav_company_logo = models.ImageField(upload_to='images/contacts', blank=True, null=True)
    footer_company_logo = models.ImageField(upload_to='images/contacts', blank=True, null=True)
    main_page_image = models.ImageField(upload_to='images/contacts', blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    company_main_page_title = models.TextField(max_length=100, blank=True, null=True)
    company_description = models.TextField(blank=True, null=True)
    def save(self, *args, **kwargs):
        if not self.pk and Footer.objects.exists():
            raise ValidationError('There is can be only one Footer instance')
        return super(Footer, self).save(*args, **kwargs)