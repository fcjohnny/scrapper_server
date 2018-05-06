from django.db import models

# Create your models here.

class Quote(models.Model):
  quotation_date = models.DateTimeField('quotation date')
  room_date = models.DateField('room date')
  room_type = models.CharField(max_length=200)
  availability = models.BooleanField(default=False)
  currency = models.CharField(max_length=20)
  quoted_price = models.DecimalField(max_digits=12,decimal_places=2)
