from django.db import models

# Create your models here.
class RegModel(models.Model):
    eid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=120)
    age=models.IntegerField()
    email=models.EmailField(unique=True)
    experience=models.IntegerField()

    def __str__(self):
        return self.name

class Person(models.Model):
    firstname=models.CharField(max_length=100) 
    secondname=models.CharField(max_length=100)   


class DeptModel(models.Model):
    name=models.CharField(max_length=120)
    description=models.CharField(max_length=300)
    office_no=models.IntegerField()


class Manager(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.IntegerField()
    pic=models.ImageField(upload_to='profilepic',null=True)   