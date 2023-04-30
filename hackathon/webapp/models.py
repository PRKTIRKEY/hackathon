from django.db import models

# Create your models here.
class book(models.Model):
    Contact_Number = models.CharField(max_length  = 15)
    Pick_Up_Point = models.TextField()
    Destination = models.TextField()
    Number_of_Passenger = models.CharField(max_length = 10)
    Mode_of_Payment = models.TextField()

class Pre_Book(models.Model):
    Contact_Number = models.CharField(max_length = 15)
    Date = models.DateField()
    Time = models.TimeField()
    Pick_Up_Point = models.TextField()
    Destination = models.TextField()
    Mode_of_Payment = models.TextField()

