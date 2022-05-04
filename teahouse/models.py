from enum import Enum

from django.core.validators import MaxLengthValidator
from django.db import models


# Create your models here.
class TeaCategory(Enum):
    GREEN = "Green"
    BLACK = "Black"
    OOLONG = "Oolong"
    SHENG_PUER = "Sheng Pu'er"
    SHU_PUER = "Shu Pu'er"
    WHITE = "White"
    AGED_WHITE = "Aged White"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)


class Origin(models.Model):
    country = models.CharField(max_length=60)
    region = models.CharField(max_length=60)

    def __str__(self):
        return f'{self.country}, {self.region}'


class Preperation(models.Model):
    teaware = models.CharField(max_length=60)
    description = models.TextField(max_length=500, blank=True,
                                   validators=[MaxLengthValidator(500)])
    gramms_per_100ml = models.IntegerField()
    steepings = models.IntegerField()
    steeptime_in_sec = models.IntegerField()
    temperature = models.IntegerField()

    def __str__(self):
        return f"""
        Teaware: {self.teaware} \n
        Description: {self.description} \n
        {self.gramms_per_100ml} per 100ml \n
        max. steepings: {self.steepings} \n
        steeptime: {self.steeptime_in_sec}s \n
        temperature: {self.temperature}°C \n
        """


class Tea(models.Model):
    name = models.CharField(max_length=60)
    category = models.CharField(max_length=20, choices=TeaCategory.choices())
    cultivar = models.CharField(max_length=60)
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE)
    harvested = models.DateField()
    preperations = models.ManyToManyField(Preperation)

    def __str__(self):
        origin_str = f"from {self.origin.region} in {self.origin.country}"

        return f"""
        {self.name} - {self.category}
        Cultivar: {self.cultivar},
        {origin_str},
        Harvested: {self.harvested.isoformat()}
        """
