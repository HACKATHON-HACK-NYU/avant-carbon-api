from django.db import models

# Create your models here.
class Card(models.Model):
    id = models.AutoField(primary_key=True)
    card_number = models.CharField(max_length=100,blank=True,null=True)
    expiry_month =  models.IntegerField()
    expiry_year =  models.IntegerField()
    cvv =  models.IntegerField(unique=True)

    def __str__(self):
        return str(self.id)
  
class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    # the card this transaction is on
    card_number = models.CharField(max_length=100,blank=True,null=True)
    date = models.DateField()
    merchant_description = models.CharField(max_length = 30)
    amount = models.DecimalField(decimal_places=2,max_digits=99)	
    
    def __str__(self):
        return str(self.id)
