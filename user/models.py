from pyexpat import model
from turtle import onclick
from django.db import models
from dashboard.models import Card
# Create your models here.
class UserAccount(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100,blank=True,null=True)
    last_name = models.CharField(max_length=100, blank=True,null=True)
    username =  models.CharField(max_length=200, blank=True)
    email = models.EmailField(unique=True)
    password = models.TextField()
    created =  models.DateTimeField(auto_now_add=True)
    modified =  models.DateTimeField(auto_now=True)
    cards = models.ForeignKey(Card, null= True,blank=True, on_delete=models.CASCADE)
    is_authenticated = model
    def __str__(self):
        return str(self.id)
