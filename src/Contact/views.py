from django.shortcuts import render
from Contact.forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def contact(request):
    form = ContactForm(request.POST or None)
    title = "Contact"
    confirm_message = None

    if form.is_valid():
        myMessage = "%s %s" %(form.cleaned_data['comment'], form.cleaned_data['name'])

        send_mail(
            "My Site's Form Email",
            myMessage,
            form.cleaned_data['email'],
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        form = None
        title = "Thanks!"
        confirm_message = "We'll get back to you as soon as we can, amigo."

    context = {
        'title': title,
        'form': form,
        'confirm_message': confirm_message,
    }

    return render(request, "contact.html", context)
