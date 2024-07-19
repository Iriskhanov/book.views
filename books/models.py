from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    image = models.FileField(upload_to='static/images', blank=True, null=True)
    description = models.TextField(max_length=255, blank=True, null=True)

    def __repr__(self):
        return self.name
