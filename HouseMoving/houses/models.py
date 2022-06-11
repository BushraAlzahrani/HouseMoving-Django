from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class House(models.Model):
    ''' this model is for storing house information '''

    previous_address = models.CharField()
    new_address = models.CharField()
    city = models.CharField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Appointment(models.Model):
    ''' this model is for storing appointment reservation information '''

    house = models.ForeignKey(House, on_delete=models.CASCADE)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    reservation_date= models.DateTimeField()

class Belongings(models.Model):
    ''' this model is for storing the house's belongings information '''

    house = models.ForeignKey(House, on_delete=models.CASCADE)
    name= models.CharField()#(couch, wardrobe, silverware...)
    type_belonging = models.CharField() #choices (furniture, kitchenware, clothes, toys, or other can be written )
    room= models.CharField() #choices (livingroom, kitchen, bedroom, kids room)

'''
class PackingSupplies (models.Model):
    this model is for storing the packing supplies needed for packing the belongings 

    material =models.CharField() #(cardboard, bubble-wrap, tissue-paper)
    quantity = models.IntegerField()
'''

class MovingTruck(models.Model):
    ''' this model is for storing the trucks available to move the belongings '''

    house = models.ForeignKey(House, on_delete=models.CASCADE)
    Size = models.CharField() #choices?
    quantity = models.IntegerField()
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
