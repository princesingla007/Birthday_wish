from django.db import models

# Create your models here.
class Img(models.Model):
    title=models.CharField(max_length=200,null=True)
    image=models.ImageField(upload_to="birthday/")

    def __str__(self):
        return self.title

class Cake(models.Model):
    img=models.ImageField(upload_to='cake/')
    knife = models.ImageField(upload_to='knife/', null=True, blank=True)    