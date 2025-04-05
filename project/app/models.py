from django.db import models

class Book(models.Model):
   tittle = models.CharField(max_length=100)
   author = models.CharField(max_length=50)
   publication_date = models.DateField()





