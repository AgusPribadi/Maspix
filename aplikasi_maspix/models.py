# aplikasi_maspix/models.py

from django.db import models

class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio_images/')
    description = models.TextField()

    def __str__(self):
        return self.title

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery_images/')
    caption = models.CharField(max_length=200)

    def __str__(self):
        return self.caption

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/', blank=True, null=True)

    def __str__(self):
        return self.title