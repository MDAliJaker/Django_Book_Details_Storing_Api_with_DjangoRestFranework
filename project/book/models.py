from django.db import models


class Book(models.Model):
    Name = models.CharField(max_length=255)
    Author_Name = models.CharField(max_length=255)
    description = models.TextField()
    Date_of_publish = models.DateField()

    def __str__(self):
        return self.title