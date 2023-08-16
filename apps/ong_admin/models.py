from django.db import models

# Create your models here.
class Expenses(models.Model):
    title = models.CharField(_("title"), max_length=50, blank=False)
    description = description = models.TextField(_('description'))
    amount_spent = models.DecimalField(_('amount spent'), max_digits=6, decimal_places=2, blank=False)