from django.db import models

# Create your models here.


class studentregister(models.Model):
    sname=models.CharField(max_length=50,null=True,blank=True)    #student name
    email=models.EmailField(null=True,blank=True)
    phno=models.IntegerField(null=True,blank=True)
    img=models.ImageField(upload_to='student/',null=True,blank=True)   #image of student
    stid=models.CharField(max_length=15,unique=True,null=True,blank=True)     #student id
    paswrd=models.CharField(max_length=8,null=True,blank=True)   #student's password for login
    dob=models.DateField(null=True,blank=True)
    adrs=models.TextField(null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    fname=models.CharField(max_length=50,null=True,blank=True)    #father name
    mname=models.CharField(max_length=50,null=True,blank=True)    #mother name
    admno=models.IntegerField(null=True,blank=True)  #admission number of student in college
    jdate=models.DateField(null=True,blank=True)     #date of joining
    dpt=models.CharField(max_length=25,null=True,blank=True)       #department
    bloodgrp=models.CharField(max_length=5,null=True,blank=True)
    GENDER_CHOICES=(
        ('Male','male'),
        ('Female','female'),
        ('Others','others'),
    )
    gender=models.CharField(max_length=15,choices=GENDER_CHOICES)
    parentno=models.IntegerField(null=True,blank=True)

class parentregister(models.Model):
    pname=models.CharField(max_length=50,null=True,blank=True)
    svname=models.ForeignKey(studentregister,on_delete=models.CASCADE,null=True,blank=True)
    adrs=models.TextField(null=True,blank=True)
    phno=models.IntegerField(null=True,blank=True)
    pid=models.CharField(max_length=15,unique=True,null=True,blank=True)
    pas=models.CharField(max_length=8,null=True,blank=True)
    
class rooms(models.Model):
    roomno=models.CharField(max_length=10,unique=True,null=True,blank=True)
    stname=models.ForeignKey(studentregister,on_delete=models.CASCADE,null=True,blank=True)
    status=models.BooleanField(default=False)
    stcount=models.IntegerField(null=True,blank=True)
    





    