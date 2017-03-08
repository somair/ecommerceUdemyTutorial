from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from allauth.account.signals import user_logged_in, user_signed_up
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

# Models
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,null=True,blank=True)
    name = models.CharField(max_length=120)
    description = models.TextField(default='default description')

    def __unicode__(self):
        return self.name

class StripeUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,null=True,blank=True)
    stripeUserID = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.user.username

# Receivers
def profileCallback(sender, request, user, **kwargs):
    userProfile, created = Profile.objects.get_or_create(user=user)
    if created:
        userProfile.name = user.username
        userProfile.save()

def stripeCallback(sender,request,user,**kwargs):
    stripeUser, created = StripeUser.objects.get_or_create(user=user)
    if stripeUser.stripeUserID is None or stripeUser.stripeUserID == "":
        customerCreationResponse = stripe.Customer.create(email=user.email)
        stripeUser.stripeUserID = customerCreationResponse["id"] #creates a Swipe Customer ID
        stripeUser.save()


# Creating Signals (Connecting senders and receivers)
user_signed_up.connect(profileCallback)
user_logged_in.connect(stripeCallback)
user_signed_up.connect(stripeCallback)
