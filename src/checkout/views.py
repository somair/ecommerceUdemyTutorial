from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings
import stripe

# Set your secret key: remember to change this to your live secret key in production
# See your keys here: https://dashboard.stripe.com/account/apikeys
stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def checkout(request):
    publishKey = settings.STRIPE_PUBLISHABLE_KEY
    if request.method == 'POST':
        # Token is created using Stripe.js or Checkout!
        # Get the payment token submitted by the form:
        token = request.POST['stripeToken']

        # Charge the user's card:
        #charge = stripe.Charge.create(
        #    amount=1000, #in cents!!!
        #    currency="usd",
        #    description="Example charge",
        #    source=token,
        #)

        # Charge a customer:
        customerID = request.user.stripeuser.stripeUserID # The logged in customer's ID
        customer = stripe.Customer.retrieve(customerID)  # Retrieve the logged in from Swipe customer using customer ID
        customer.sources.create(source=token)  # Create a new source for this customer to charge
        stripe.Charge.create(
            amount=100000,
            currency="usd",
            customer=customerID,  # Charge the customer directly
            description="Example Charge"
        )


    context = {
        'publishKey': publishKey,
    }
    return render(request, "checkout.html", context)