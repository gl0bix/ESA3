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


class Origin(models.Model):
    country = models.CharField(max_length=60)
    region = models.CharField(max_length=60)


class Preperation(models.Model):
    teaware = models.CharField(max_length=60)
    description = models.TextField(max_length=500, blank=True,
                                   validators=[MaxLengthValidator(500)])
    gramms_per_100ml = models.IntegerField()
    steepings = models.IntegerField()
    steeptime_in_sec = models.IntegerField()


class Tea(models.Model):
    name = models.CharField(max_length=60)
    category = models.CharField(max_length=20, choices=[{"tag": tag, "value": tag.value} for tag in TeaCategory])
    cultivar = models.CharField(max_length=60)
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE)
    harvested = models.DateField()
    preperation = models.ManyToManyField(Preperation)

    def __str__(self):
        origin_str = f"from {self.origin.region} in {self.origin.country}"
        preperation_str = "\n- ".join([f"""
        Teaware: {p.teaware}"
        Description: {p.description}
        {p.gramms_per_100ml} per 100ml
        max. steepings: {p.steepings}
        steeptime: {p.steeptime}s
        """
                                       for p in self.preperation.all()])
        return f"""
        {self.name} - {self.category.get("value")}
        Cultivar: {self.cultivar}
        Origin: {origin_str}
        Harvested: {self.harvested.isocalendar()}
        Recommended Preperations:
        {preperation_str}
        """
