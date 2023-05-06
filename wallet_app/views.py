from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .models import Currency, Wallet
from .tasks import currency_update_task
from .service import currency_update


class MainPage(ListView):
    model = Wallet
    template_name = "wallet_app/index.html"

    def get_queryset(self):
        return Wallet.objects.filter(user=self.request.user)


# def cur_update(request):
#     currency_update_task.delay()
#     return HttpResponse("ok")
#
#
# class Currencies(ListView):
#     model = Currency
#     template_name = "wallet_app/currencies.html"
#
#     def get_queryset(self):
#         return Currency.objects.all()
