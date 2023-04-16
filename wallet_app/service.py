import json

from _decimal import Decimal
from django.core.exceptions import ObjectDoesNotExist

from .models import Currency


def currency_update_or_create(code, value):
    print("currency_update_or_create")
    try:
        cur = Currency.objects.get(code=code)
        cur.convertion_rate = Decimal(value)
        cur.save()
        print(f'{code} - {value}')
        print(f'{cur.code} - {cur.convertion_rate}')
    except ObjectDoesNotExist:
        new_cur = Currency(name=code, code=code, convertion_rate=value)
        new_cur.save()
    except Exception as e:
        print(e)


def currency_update():
    with open('data.json') as file:
        json_read = file.read()
        data = json.loads(json_read)
        for currency in data["data"]:
            currency_update_or_create(code=currency, value=data["data"][currency]["value"])
    return "Ok"

