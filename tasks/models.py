from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.IntegerField()
    password = models.IntegerField()
    grupo = models.CharField(max_length=50)


