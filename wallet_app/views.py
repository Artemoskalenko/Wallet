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
        name = request.POST.get('name')
        color = request.POST.get('color')
        selected_type = request.POST.get('selectedType').strip()
        quantity = float(request.POST.get('quantity'))
        selected_currency = Currency.objects.get(code=request.POST.get('selectedCurrency'))
        exclude_from_stat = True if request.POST.get('exclude_from_stat') else False
        # for item in request.POST:
        #     print(f"{item} == {request.POST.get(item).strip()}")
        new_account = Wallet.objects.create(user=request.user, name=name, color=color, account_type=selected_type,
                                            balance=quantity, currency=selected_currency,
                                            exclude_from_statistic=exclude_from_stat)
        new_account.save()
        # print(name)
        # print(color)
        # print(selected_type)
        # print(quantity)
        # print(selected_currency)
        # print(True if request.POST.get('exclude_from_stat') else False)

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
