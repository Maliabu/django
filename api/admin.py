from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(SupportedLanguage)
admin.site.register(SupportedCountry)
admin.site.register(Currency)
admin.site.register(TimeZone)
admin.site.register(UserProfile)
admin.site.register(Module)
admin.site.register(SideMenu)
admin.site.register(DashboardMenu)
admin.site.register(PaymentType)
admin.site.register(PaymentMethod)
admin.site.register(PaymentOption)
admin.site.register(PaymentOptionField)
admin.site.register(PaymentOptionSetting)
admin.site.register(PaymentOptionSupport)
admin.site.register(PaymentTypeOption)
admin.site.register(RegionalPaymentType)
admin.site.register(PaymentTypeSetting)
admin.site.register(DepositType)
admin.site.register(DepositTime)
admin.site.register(AccountType)
admin.site.register(Account)
admin.site.register(LedgerEntry)