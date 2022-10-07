from django.db import models
from authentications.models import supervisor , Users
# Create your models here.
from django.utils import timezone

class VolunteerDay(models.Model):
    Supervisor= models.ForeignKey(supervisor , on_delete=models.CASCADE)
    street = models.CharField(max_length=50,blank= False)
    start= models.CharField(max_length=50,blank= False)
    finish =models.CharField(max_length=50,blank= False)
    date = models.CharField(max_length=50,blank= False)
    createdAt= models.DateField(auto_created=True, default=timezone.now)
    modofiedAt= models.DateField(auto_created=True , auto_now=True)
    def __str__(self):
        return self.street



class Comment(models.Model):
    user = models.ForeignKey(Users , on_delete=models.CASCADE)
    content = models.CharField(max_length=500, blank=False)

    createdAt= models.DateField(auto_created=True, default=timezone.now)
    modofiedAt = models.DateField(auto_created=True, auto_now=True)

    def __str__(self):
        return self.user.name


class advertisement(models.Model):
    user=models.ForeignKey(Users , on_delete=models.CASCADE,blank=False)
    title=models.CharField(max_length=50, blank=False)
    content= models.CharField(max_length=500, blank=False)
    createdAt= models.DateField(auto_created=True, default=timezone.now)
    modofiedAt = models.DateField(auto_created=True, auto_now=True)
    def __str__(self):
        return self.title

class gadeget(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE,blank=False)
    name = models.CharField(max_length=50,blank=False)
    amount= models.IntegerField(blank=False)

    createdAt= models.DateField(auto_created=True, default=timezone.now)
    modofiedAt = models.DateField(auto_created=True, auto_now=True)
    def __str__(self):
        return self.name

class report(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, blank=False)
    volDate= models.ForeignKey(VolunteerDay,on_delete=models.CASCADE,blank=False)
    moneySpent= models.IntegerField(blank=False)
    moneyDonated = models.IntegerField(blank=False)

    createdAt= models.DateField(auto_created=True, default=timezone.now)
    modofiedAt = models.DateField(auto_created=True, auto_now=True)

    def __str__(self):
        return self.volDate.street

