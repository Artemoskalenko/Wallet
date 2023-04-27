import json

from _decimal import Decimal
from django.core.exceptions import ObjectDoesNotExist

from .models import Currency
from .service import currency_update
from config.celery import app


@app.task
def currency_update_task():
    currency_update()
