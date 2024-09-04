from django.db import models

class Movie(models.Model):
    movie = models.CharField(max_length=50)
    hall = models.CharField(max_length=10)
    reservation = models.DateField()

class Guest(models.Model):
    name = models.CharField(max_length=20)
    mobile = models.CharField(max_length=11)

class Reservation(models.Model):
    guest = models.ForeignKey(Guest, related_name='reservations', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='reservations', on_delete=models.CASCADE)
