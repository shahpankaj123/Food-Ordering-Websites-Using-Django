from django.db import models


# Create your models here.

class category(models.Model):
    features_CHOICES = (
        ('Y', 'yes'),
        ('N', 'no'),
    )
    title=models.CharField(max_length=100)
    img=models.FileField(upload_to='images/')
    features=models.CharField(choices=features_CHOICES,max_length=1)
    active=models.CharField(choices=features_CHOICES,max_length=1)
    
    def __str__(self):
        return str(self.id)
    
class food(models.Model):
    ftitle=models.CharField(max_length=50)
    fdesc=models.CharField(max_length=100)
    price=models.IntegerField()
    fimg=models.FileField(upload_to='food/') 
    features_CHOICES = (
        ('Y', 'yes'),
        ('N', 'no'),
    )
    features=models.CharField(choices=features_CHOICES,max_length=1)
    active=models.CharField(choices=features_CHOICES,max_length=1)
    cid= models.ForeignKey(category, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)
    
    
class odeer(models.Model):
    food=models.CharField(max_length=50)
    price=models.IntegerField()
    qty=models.IntegerField()
    totalprice=models.IntegerField()
    oder_date=models.DateField()
    status_choice=(
        ('Odered','Odered'),
        ('Deliverd','Deliverd'),
        ('Delivering','Delivering'),
        ('Canceled','Canceled'),
        )
    status=models.CharField(choices=status_choice,max_length=20)
    customer_name=models.CharField(max_length=40)
    customer_contact=models.IntegerField()
    customer_email=models.CharField(max_length=25)
    customer_address=models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.status)
    
       
