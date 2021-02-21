from django.db import models

#its a tabel
# Create your models here.
class Contact(models.Model):
    #gonna write the things in my form
    name = models.CharField(max_length=122) #this is column
    email = models.CharField(max_length=122)
    desc = models.TextField()   #short for description
    date = models.DateField()

    def __str__(self):
        return self.name
    