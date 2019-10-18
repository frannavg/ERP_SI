from django.db import models

class Categoria(models.Model):
    codigoFrequentador =  models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name


# Create your models here.
