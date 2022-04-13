from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


    def __str__(self):
        return self.name