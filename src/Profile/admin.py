from django.contrib import admin

# Register your models here.
from Profile import models

class ProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Profile

admin.site.register(models.Profile,ProfileAdmin)

class StripeUserAdmin(admin.ModelAdmin):
    class Meta:
        model = models.StripeUser

admin.site.register(models.StripeUser,StripeUserAdmin)