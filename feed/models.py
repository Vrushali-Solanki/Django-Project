from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
meal = (
    ('breakfast', 'BREAKFAST'),
    ('dinner', 'DINNER'),
    ('lunch', 'LUNCH'),

)

quantity = (
    ('less than 5', 'LESS THAN 5'),
    ('less than 10','LESS THAN 10'),
    ('less than 15','LESS THAN 15'),
    ('less than 20','LESS THAN 20'),
    ('less than 30','LESS THAN 30'),
    ('less than 50','LESS THAN 50'),
    ('more than 50','MORE THAN 50'),
    

)
class tweet(models.Model):
    fname = models.CharField(max_length=280,default='')
    address = models.TextField(max_length=280,default='')
    phone = models.CharField(max_length=280,default='') 
    #meal = models.ForeignKey(User,on_delete=models.CASCADE, related_name='meal') 
    meal = models.CharField(max_length=15, choices=meal, default='dinner')
    quantity= models.CharField(max_length=15, choices=quantity, default='less than 15')
    #quantity = models.ForeignKey(User,on_delete=models.CASCADE, related_name='quantity') 
    datetime = models.DateTimeField(default=timezone.now)
     

    