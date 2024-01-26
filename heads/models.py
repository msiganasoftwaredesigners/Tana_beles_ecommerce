# models.py
from django.db import models

class HeadContent(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content[:50]  