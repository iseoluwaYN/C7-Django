from django.db import models

# Create your models here.
class Cohort(models.Model):
    name = models.CharField(max_length=30, unique=True)
    priest = models.EmailField(blank=True)
    priestess = models.EmailField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name


class Native(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(blank=True, unique=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images')
    date_created = models.DateTimeField(auto_now_add=True)