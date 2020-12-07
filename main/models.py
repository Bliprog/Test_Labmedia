from django.db import models

# Create your models here.

class Client(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    country=models.CharField(max_length=50)

    def __str__(self):
        return self.pk

class PayInfo(models.Model):
    payer_id=models.ForeignKey(to=Client, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=100)
    percent=models.FloatField()
    pay_date = models.DateTimeField()

    def __str__(self):
        return self.pk