from django.utils import timezone
from django.db.models import Sum

from django.core.files.base import ContentFile

from celery import shared_task

import datetime

from rolepermissions.checkers import has_role

import pandas as pd

import io

from authentication.models import User
from ong.models import Project
from ong_admin.models import Expenses
from .models import Sheet


@shared_task(bind=True)
def create_monthly_sheet(self):
    current = timezone.now()
    month = current.month - 1 if current.month > 1 else 12
    year = current.year if current.month > 1 else current.year - 1

    projects = Project.objects \
        .filter(created_at__month=month) \
        .filter(created_at__year=year) \
        .filter(is_active=False) \
        .aggregate(total=Sum('amount_spent')) \
        .get('total') or 0

    expenses = Expenses.objects \
        .filter(date__month=month) \
        .filter(date__year=year) \
        .aggregate(total=Sum('amount_spent')) \
        .get('total') or 0
    
    users = User.objects.all()
    
    volunteers_count = len(list(filter(lambda x: has_role(x, 'voluntary'), users)))
    supporters_count = len(list(filter(lambda x: has_role(x, 'supporter'), users)))

    data = {
        'Despesas Comuns': [expenses],
        'Despesas com Ações': [projects],
        'Quantidade de Voluntários Novos': [volunteers_count],
        'Quantidade de Apoiadores Novos': [supporters_count]
    }

    df = pd.DataFrame(data)
    sheet = Sheet()

    buffer = io.BytesIO()
    df.to_excel(buffer, index=False)

    sheet.file.save(
        f'{datetime.datetime(year, month, 1).date().strftime("%Y/%m-%Y")}.xlsx',
        ContentFile(buffer.getvalue())
    )

    sheet.save()

    return True
