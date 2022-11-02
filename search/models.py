from django.db import models
from taggit.managers import TaggableManager
from accounts.models import PDFBaseUser

# Create your models here.


class Tag(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Thesis(models.Model):
    title = models.CharField(max_length=255)
    date_submitted = models.DateField(blank=True, null=True)
    abstract = models.CharField(max_length=255)
    authors = models.ManyToManyField(PDFBaseUser)
    tags = TaggableManager()

    def __str__(self):
        return self.title

