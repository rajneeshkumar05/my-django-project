from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(max_length=2)
    email_id = models.EmailField(unique=True)
    city = models.CharField(max_length=100,default="Unkownn")

    def __str__(self):
        return self.name