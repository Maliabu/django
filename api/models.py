from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date
from enumchoicefield import ChoiceEnum, EnumChoiceField
# Create your models here.
class AthousandSeparator(models.Model):
    dispaly_name = models.CharField(max_length=255)
    code_name = models.CharField(max_length=255)
    is_default = models.BooleanField(default=False)
    is_disabled = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    has_been_modified = models.BooleanField(default=False)
    last_modified = models.DateTimeField()
    def __str__(self):
       return "%s" % self.dispaly_name

class DateFormats(models.Model):
    dispaly_name = models.CharField(max_length=255)
    date_format = models.CharField(max_length=255)
    is_default = models.BooleanField(default=False)
    is_disabled = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    has_been_modified = models.BooleanField(default=False)
    last_modified = models.DateTimeField()
    def __str__(self):
       return "%s" % self.dispaly_name

class DecimalSeparator(models.Model):
    dispaly_name = models.CharField(max_length=255)
    code_name = models.CharField(max_length=255)
    is_default = models.BooleanField(default=False)
    is_disabled = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    has_been_modified = models.BooleanField(default=False)
    last_modified = models.DateTimeField()
    def __str__(self):
       return "%s" % self.dispaly_name

class SupportedLanguage(models.Model):
    lang_name = models.CharField(max_length=255)
    lang_iso_code = models.CharField(max_length=255)
    is_default = models.BooleanField(default=False)
    is_disabled = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
       return "%s" % self.lang_name

#######################################
class SupportedCountry(models.Model):
    coutry_name = models.CharField(max_length=255)
    coutry_flag = models.CharField(max_length=255)
    country_code = models.CharField(max_length=255)
    is_default = models.BooleanField(default=False)
    is_disabled = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
       return "%s" % self.coutry_name

class TimeZones(models.Model):
    country = models.ForeignKey(SupportedCountry, on_delete=models.CASCADE, null=True, blank=True)
    dispaly_name = models.CharField(max_length=255)
    code_name = models.CharField(max_length=255)
    is_default = models.BooleanField(default=False)
    is_disabled = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    has_been_modified = models.BooleanField(default=False)
    last_modified = models.DateTimeField()
    def __str__(self):
       return "%s" % self.dispaly_name

class Currency(models.Model):
    country = models.ForeignKey(SupportedCountry, on_delete=models.CASCADE, null=True, blank=True)
    currency_locale = models.CharField(max_length=255)
    currency_code = models.CharField(max_length=255)
    currency_symbol = models.CharField(max_length=255)
    exchange_rate = models.FloatField(max_length=500)
    is_indented = models.BooleanField(default=False)
    is_infront = models.BooleanField(default=True)
    decimal_points = models.IntegerField(default=2)
    is_default = models.BooleanField(default=False)
    is_disabled = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
       return "%s" % self.currency_locale

# Main Application Modules
class ModuleGroup(models.Model):
    module_group_name = models.CharField(max_length=255)
    code_name = models.CharField(max_length=255)
    sort_value = models.IntegerField()
    is_disabled = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    has_been_modified = models.BooleanField(default=False)
    last_modified = models.DateTimeField()
    def __str__(self):
        return "%s" % self.module_group_name

# Main Application Modules
class Module(models.Model):
    module_name = models.CharField(max_length=255)
    code_name = models.CharField(max_length=255)
    route_name = models.CharField(max_length=255)
    is_a_sub_module = models.BooleanField(default=False)
    has_children = models.BooleanField(default=False)
    main_module_id = models.IntegerField(null=True, blank=True)
    sort_value = models.IntegerField()
    depth = models.IntegerField()
    is_disabled = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "%s" % self.module_name

# Side Menu Modules
class SideMenu(models.Model):
    module = models.ForeignKey(Module, on_delete=models.DO_NOTHING)
    sort_value = models.IntegerField()
    is_disabled = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    has_been_modified = models.BooleanField(default=False)
    last_modified = models.DateTimeField()
    def __str__(self):
        return "%s" % self.module

# Dashboard menu model
class DashboardMenu(models.Model):
    module = models.ForeignKey(Module, on_delete=models.DO_NOTHING)
    group = models.ForeignKey(ModuleGroup, on_delete=models.DO_NOTHING, null=True, blank=True)
    sort_value = models.IntegerField()
    is_disabled = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    has_been_modified = models.BooleanField(default=False)
    last_modified = models.DateTimeField()
    def __str__(self):
        return "%s" % self.module.module_name


# User Profile
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.ForeignKey(SupportedCountry, on_delete=models.CASCADE, null=True, blank=True)
    gender = models.CharField(max_length=255, null=True, blank=True)
    phoneno = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=30, null=True, blank=True)
    email_verification_code = models.CharField(max_length=30, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.CharField(max_length=255, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=True)
    is_disabled = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "%s" % self.user

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


class PaymentType(models.Model):
    payment_name = models.CharField(max_length=200)
    code_name = models.CharField(max_length=200)
    payment_logo = models.CharField(max_length=200, null=True, blank=True)
    sort_value = models.IntegerField(default=0)
    has_standarded_charge = models.BooleanField(default=False)
    payment_charge = models.FloatField(default=0, blank=True, null=True)
    charge_in_percentage = models.BooleanField(default=True)
    charge_fees_on_user = models.BooleanField(default=True)
    is_default = models.BooleanField(default=False)
    is_disabled = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
       return "%s" % self.payment_name

class PaymentTypeSetting(models.Model):
    payment_type = models.ForeignKey(PaymentType, on_delete=models.DO_NOTHING)
    entry_name = models.CharField(max_length=500)
    entry_code_name = models.CharField(max_length=255)
    has_entry_value = models.BooleanField(default=False)
    entry_value = models.CharField(max_length=500, null=True, blank=True)
    is_required = models.BooleanField(default=True)
    is_default = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_disabled = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    has_been_modified = models.BooleanField(default=False)
    def __str__(self):
        return "[%s] %s : %s" % (str(self.payment_type), self.entry_name, str(self.entry_value))


class DepositType(models.Model):
    type_name = models.CharField(max_length=200)
    code_name = models.CharField(max_length=200)
    is_default = models.BooleanField(default=False)
    is_disabled = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
       return "%s" % self.type_name

class DepositTime(models.Model):
    time_name = models.CharField(max_length=200)
    code_name = models.CharField(max_length=200)
    is_default = models.BooleanField(default=False)
    is_disabled = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
       return "%s" % self.time_name


class AccountType(models.Model):
    type_name = models.CharField(max_length=200)
    code_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=True, blank=True)
    sort_value = models.IntegerField(default=0)
    is_default = models.BooleanField(default=False)
    is_disabled = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
       return "%s" % self.type_name

class DrCr(ChoiceEnum):
    dr = "D"
    cr = "C"

class Account(models.Model):
    account_type = models.ForeignKey(AccountType, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=500)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE) # Default currency
    opening_balance = models.FloatField(default=0)
    account_no = models.CharField(max_length=300)
    is_operational_account = models.BooleanField(default=False)
    is_cash_account = models.BooleanField(default=False)
    is_reconcilable = models.BooleanField(default=False)
    allow_over_drafts = models.BooleanField(default=False)
    narration = models.CharField(max_length=3000, null=True, blank=True)
    is_disabled = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    is_editable = models.BooleanField(default=True)
    is_deletable = models.BooleanField(default=True)
    has_been_modified = models.BooleanField(default=False)
    last_modified = models.DateTimeField()
    def __str__(self):
        return "%s" % self.account_name


# Ledger Entries or Account Entries or Account Ledgers   
class LedgerEntry(models.Model):
    ledger_no = models.IntegerField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    entry_type = EnumChoiceField(DrCr, default=DrCr.dr)
    is_adjusting_entry = models.BooleanField(default=False)
    amount = models.FloatField(default=0)
    narration = models.CharField(max_length=5000, null=True, blank=True)
    is_disabled = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return "%s - %s" % (self.account, self.amount)