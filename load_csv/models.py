from django.db import models


class Documents(models.Model):
    NUMDOS = models.CharField(max_length=100)
    NUMDOSVERLING = models.CharField(max_length=100)
    ANCART = models.CharField(max_length=100)
    FILIERE = models.CharField(max_length=100)
    ETAPE = models.FloatField(max_length=100)
    VERLING = models.CharField(max_length=100)
    FORMAT = models.CharField(max_length=100)
