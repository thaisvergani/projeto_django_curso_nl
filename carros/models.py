# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Fabricante(models.Model):
    nome = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.nome


class Carro(models.Model):
    name = models.CharField(max_length=300, null=True)
    price = models.DecimalField(decimal_places=2,null=True, max_digits=5)
    year =  models.IntegerField(null=True)
    model = models.CharField(max_length=300, null=True)
    fabricante = models.ForeignKey(Fabricante, null=True)

    def __str__(self):
        return self.name

