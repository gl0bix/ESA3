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
        Teaware: {self.teaware}"
        Description: {self.description}
        {self.gramms_per_100ml} per 100ml
        max. steepings: {self.steepings}
        steeptime: {self.steeptime_in_sec}s
        temperature: {self.temperature}°C
        """


class Tea(models.Model):
    name = models.CharField(max_length=60)
    category = models.CharField(max_length=20, choices=TeaCategory.choices())
    cultivar = models.CharField(max_length=60)
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE)
    harvested = models.DateField()
    preperation = models.ManyToManyField(Preperation)

    def __str__(self):
        origin_str = f"from {self.origin.region} in {self.origin.country}"
        preperation_str = "\n- ".join([p.__str__() for p in self.preperation.all()])

        return f"""
        {self.name} - {self.category[1]}
        Cultivar: {self.cultivar}
        Origin: {origin_str}
        Harvested: {self.harvested.isocalendar()}
        Recommended Preperations:
        {preperation_str}
        """
