from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class House(models.Model):
    ''' this model is for storing house information '''
    name = models.CharField(max_length=150)
    previous_address = models.CharField(max_length=250) # street, neighborhood
    new_address = models.CharField(max_length=250) # street, neighborhood
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    ''' this model is for storing appointment reservation information '''

    house = models.ForeignKey(House, on_delete=models.CASCADE)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    reservation_date= models.DateTimeField()

class Belongings(models.Model):
    ''' this model is for storing the house's belongings information '''
    class BelongingType(models.TextChoices):
        FURNITURE = 'furniture'
        KITCHENWARE = 'kitchenware'
        CLOTHES = 'clothes'
        TOYS = 'toys'
        ELECTRONICS= 'electronics'

    class Room(models.TextChoices):
        LIVINGROOM= 'livingroom'
        GUESTROOM= 'guestroom'
        KITCHEN= 'kitchen'
        BEDROOM = 'bedroom'
        KIDSROOM = 'kidsroom'

    house = models.ForeignKey(House, on_delete=models.CASCADE)
    name= models.CharField(max_length=50)#(couch, wardrobe, silverware...)
    type_belonging = models.CharField(choices=BelongingType.choices, max_length=20)
    room= models.CharField(choices=Room.choices, max_length=20)

    def __str__(self):
        return self.name

class MovingTruck(models.Model):
    ''' this model is for storing the trucks available to move the belongings '''

    house = models.ForeignKey(House, on_delete=models.CASCADE)
    Size = models.CharField(max_length=20)
    quantity = models.IntegerField()
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
