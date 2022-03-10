from django.db import models

class Contact(models.Model):
    email = models.TextField(max_length=40)
    pw = models.TextField(max_length=20)

    def __str__(self):
        return self.email
    

# Create your models here.
