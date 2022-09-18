from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=400)
    email = models.EmailField(max_length=300)
    subject = models.TextField()
    message = models.TextField()
    def __str__(self):
        return self.name
