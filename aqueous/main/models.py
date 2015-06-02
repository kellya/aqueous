from django.db import models


class Type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    phone = models.CharField(
        max_length=32,
        null=True,
        blank=True,
    )
    webpage = models.URLField(
        null=True,
        blank=True,
    )
    email = models.EmailField(
        null=True,
        blank=True,
    )
    address = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Tank(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    date_established = models.DateField()
    volume = models.IntegerField()
    notes = models.TextField(
        null=True,
        blank=True,
    )
    type = models.ForeignKey('Type')
    manufacturer = models.ForeignKey(
        'Manufacturer',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name
