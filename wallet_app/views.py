from django.http import HttpResponse
from django.shortcuts import render

from .models import Currency
from .tasks import currency_update_task
from .service import currency_update


def home(request):
    currency_update_task.delay()
    return HttpResponse("ok")


def check(request):
    value = Currency.objects.get(code="UAH")
    return HttpResponse(f"{value.convertion_rate}")


def change(request):
    cur = Currency.objects.get(code="UAH")
    cur.convertion_rate = 33
    cur.save()
    return HttpResponse(f"{cur.convertion_rate}")


def json_view(request):
    currency_update()
    return HttpResponse("OK")
