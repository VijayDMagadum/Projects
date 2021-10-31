from django.db import models

# Create your models here.
class user(models.Model):
    id=models.AutoField(primary_key=True)
    email=models.EmailField(max_length=50, null=True)
    password=models.CharField(max_length=50,null=True )
    password2=models.CharField(max_length=50,null=True )
    fname=models.CharField(max_length=50,null=True )
    lname=models.CharField(max_length=50,null=True )

class books(models.Model):
    bookname=models.CharField(max_length=50,unique=True)
    bookid=models.AutoField(primary_key=True,unique=True)
