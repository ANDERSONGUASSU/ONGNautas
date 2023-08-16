from django.db import models

# Create your models here.
class Expenses(models.Model):
    title = models.CharField(max_length=50, blank=False)
    description = description = models.TextField()
    amount_spent = models.DecimalField(max_digits=6, decimal_places=2, blank=False)