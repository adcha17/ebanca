from django.contrib import admin
from core.models import Client, Account, CreditCard, User


admin.site.register(Client)
admin.site.register(Account)
admin.site.register(CreditCard)
admin.site.register(User)