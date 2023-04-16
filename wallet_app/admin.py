from django.contrib import admin
from .models import Currency, Wallet, BalanceHistory, Category, Subcategory, Record


admin.site.register(Currency)
admin.site.register(Wallet)
admin.site.register(BalanceHistory)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Record)