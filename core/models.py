from django.db import models

# Create your models here.
class GeneralSettings(models.Model): #database de bir tablo old belirtiliyor.
    name = (models.CharField
        (
        default='',
        max_length=254,
        blank=True,
    ))
    description = models.CharField(
        max_length=254,
        default='',
        blank=True,
    )
    parameter=models.CharField(
        max_length=254,
        default='',
        blank=True,
    )
    updated_date =models.DateField(
        blank=True,
        auto_now=True,
    )
    created_date =models.DateField(
        blank=True,
        auto_now_add=True, #bir kere kayıt alıyor
    )
