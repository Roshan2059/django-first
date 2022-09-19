from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=400)
    email = models.EmailField(max_length=300)
    subject = models.TextField()
    message = models.TextField()
    def __str__(self):
        return self.name

class Feedback(models.Model):
    name = models.CharField(max_length=300)
    post = models.TextField()
    comment = models.TextField()
    image = models.TextField()

    def __str__(self):
        return self.name

class price(models.Model):
    economy = models.IntegerField()
    business = models.IntegerField()
    premium = models.IntegerField()
    exclusive = models.IntegerField()

    def __str__(self):
        return f"{self.economy} {self.business} {self.premium} {self.exclusive}"

class Service(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=300)
    description = models.TextField()

    def __str__(self):
        return self.name




