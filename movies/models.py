from django.db import models
from enum import Enum




class Hall(models.Model):

    class HallType(models.IntegerChoices):
        basic = 1,"Basic"
        three_D = 2,"3D"
        VIP = 3,"VIP"

    hall_number = models.IntegerField(null=False)
    type = models.SmallIntegerField(null=False, default = HallType.basic, choices=HallType.choices)
    seats = models.SmallIntegerField(null=False)
    price = models.IntegerField(null=False)
    hall_name = models.CharField(max_length=100,null=False)

    def __str__(self):
        return str(self.hall_number)


class Movie(models.Model):

    name = models.CharField(max_length=200, null=False)
    genre = models.CharField(max_length=200, null=False)
    length = models.SmallIntegerField(null=False)
    year = models.SmallIntegerField(null=False)
    image = models.ImageField(null=True, blank=True, default='/placeholder.png')
    age_restrictions= models.CharField(max_length=200, null=False, default="12+")
    trailer= models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.name

class Screening(models.Model):
    movie_id = models.ForeignKey(Movie,on_delete=models.CASCADE)
    hall_id= models.ForeignKey(Hall,on_delete=models.CASCADE)
    screening_time =models.DateTimeField()
    # tickets_left = models.SmallIntegerField(null=False)

