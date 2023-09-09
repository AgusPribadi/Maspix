from django.db import models

class Portfolio(models.Model):
    CATEGORY_CHOICES = (
        ('Website', 'Website'),
        ('Desain', 'Desain'),
        ('Machine Learning', 'Machine Learning'),
    )

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio_images/')
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, null=True, blank=True)

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