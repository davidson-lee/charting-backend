from django.db import models

# Create your models here.
class Corporation(models.Model):
    ticker = models.CharField(max_length=5)
    name = models.CharField(max_length=100)
    description = models.TextField(default='')

    def __str__(self):
        return self.ticker

class Trades(models.Model):
    corporation = models.ForeignKey(
        Corporation,
        on_delete=models.CASCADE
    )
    price = models.DecimalField(max_digits=4, decimal_places=2)
    time = models.SmallIntegerField()

    def __str__(self):
        return str(self.price)