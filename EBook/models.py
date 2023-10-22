from django.db import models

# Create your models here.
class ChuDe(models.Model):
    MaCD = models.FloatField()
    TenCD = models.CharField(max_length=50)
    def __str__(self):
        return 