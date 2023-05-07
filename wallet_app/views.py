from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView

from .models import Currency, Wallet
from .tasks import currency_update_task
from .service import currency_update


class MainPage(ListView):
    model = Wallet
    template_name = "wallet_app/index.html"

    def get_queryset(self):
        return Wallet.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["currencies"] = Currency.objects.all()
        return context


class CreateAccount(CreateView):
    def post(self, request, *args, **kwargs):
        # field1 = request.POST.get('field1')
        color = request.POST.get('color')
        quantity = request.POST.get('quantity')
        # print(color)
        # print(quantity)
        for item in request.POST:
            print(item)



        return redirect('main')

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
