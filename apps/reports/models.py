from django.db import models
from authentication.validators import cep_validator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

import datetime


class Report(models.Model):

    title = models.CharField(max_length=30, blank=False)
    description = models.TextField()

    cep = models.CharField(max_length=8, blank=False, default='Sem CEP', validators=[cep_validator])
    address = models.CharField(max_length=64, blank=False, default='Não definido')
    complement = models.CharField(max_length=24, blank=True)

    evidence_image = models.ImageField(upload_to='denouncements')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Denúncia'
        verbose_name_plural = 'Denúncias'


class Sheet(models.Model):

    file = models.FileField(_('file'), upload_to='sheets')
    
    date = models.DateField(_('date'), default=timezone.now() - datetime.timedelta(days=timezone.now().day))

    def __str__(self) -> str:
        return f'Relação de {self.date.strftime("%m/%Y")}'
    
    class Meta:

        verbose_name = _('Sheet')
        verbose_name_plural = _('Sheets')
