from django.db import models


# Create your models here.
class Type(models.Model):
    Province_code = models.CharField(max_length=5)
    Province_name = models.CharField(max_length=50)
    Administrative_area_code = models.CharField(max_length=50)
    Single_Family_Residence = models.CharField(max_length=50)
    Multi_family_housing = models.CharField(max_length=50)
    Industry = models.CharField(max_length=50)
    Public_service = models.CharField(max_length=50)
    Other_build = models.CharField(max_length=50)
    Others = models.CharField(max_length=50)
