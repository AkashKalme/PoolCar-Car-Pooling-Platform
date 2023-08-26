from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.username)


class Journey(models.Model):
    source = models.CharField(max_length=100, blank=False)
    destination = models.CharField(max_length=100, blank=False)
    date_of_journey = models.DateField(blank=False)
    number_of_seats = models.IntegerField(blank=False)
    cost_per_person = models.IntegerField(blank=False)

    def __str__(self):
        return f"{self.source}-{self.destination}"


class Car(models.Model):
    car_name = models.CharField(max_length=100, blank=False)
    vehicle_number = models.CharField(max_length=10, blank=False)

    def __str__(self):
        return self.car_name


class Driver(models.Model):
    driver_name = models.CharField(max_length=100, blank=False)
    driver_licence_number = models.CharField(max_length=16, blank=False)

    def __str__(self):
        return self.driver_name


class Ride(models.Model):
    publisher = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='rides')
    journey_details = models.ForeignKey(Journey, on_delete=models.CASCADE)
    car_details = models.ForeignKey(Car, on_delete=models.CASCADE)
    driver_details = models.ForeignKey(Driver, on_delete=models.CASCADE)
    poolers = models.ManyToManyField(Profile)

    def __str__(self):
        return f"{str(self.publisher)} ({self.journey_details.source}-{self.journey_details.destination})"
