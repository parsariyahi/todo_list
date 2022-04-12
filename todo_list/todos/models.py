from django.db import models

# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name