from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(SupportedLanguage)
admin.site.register(SupportedCountry)
admin.site.register(Currency)