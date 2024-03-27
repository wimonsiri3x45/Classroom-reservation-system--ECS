from django.db import models

# Create your models here.
class User(models.Model):
    studentid = models.IntegerField()
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    statususer = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.studentid)+ "," + self.firstname + self.lastname

class Room(models.Model):
    roomname = models.CharField(max_length=100)
    typeroom = models.CharField(max_length=100)
    seats = models.IntegerField()
    location = models.CharField(max_length=100)
    equipment = models.CharField(max_length=100)
    imgroom = models.ImageField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.roomname
    
class Booking(models.Model):
    classroom = models.CharField(max_length=100)
    namebooker = models.CharField(max_length=100)
    seatsuse = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    note = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.classroom + "," + self.namebooker + "," + str(self.datetime )