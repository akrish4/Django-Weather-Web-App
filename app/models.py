from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email=models.EmailField()
    number=models.IntegerField()
    description=models.TextField()

    

    def __str__(self):
        return self.email+" " +"by"+" "+self.name
    



