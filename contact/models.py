from django.db import models

# Create your models here.


class ContactUs(models.Model):
    name = models.CharField('Name', max_length=254)
    email = models.EmailField('Email', max_length=254)
    message = models.TextField('Message', max_length=2000)

    def __str__(self):
        return self.name