from django.db import models

class Passenger(models.Model):
    passenger_id = models.IntegerField(unique=True)
    sex = models.CharField(max_length=255)
    age = models.FloatField(null=True)
    parch = models.IntegerField(null=True)
    fare = models.FloatField(null=True)
    survived = models.FloatField(null=True)
    is_test = models.IntegerField(null=True)


    def __str__(self):
        return self.name

