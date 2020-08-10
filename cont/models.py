from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    phone=models.CharField(max_length=13)
    message=models.TextField()

    def __str__(self):
        return'message from ' + self.name