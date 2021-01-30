from django.db import models

# Create your models here.

class signup(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    zipcode=models.IntegerField()

    def __str__(self):
        return self.fname

class notes(models.Model):
    title=models.CharField(max_length=50)
    category=models.CharField(max_length=100)
    myfile=models.FileField(upload_to='upload')
    comments=models.CharField(max_length=500)

    def __str__(self):
        return self.title
