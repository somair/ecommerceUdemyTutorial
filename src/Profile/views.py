from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):
    return render(request, "home.html", None)

def about(request):
    return render(request, "about.html", None)

@login_required
def userProfile(request):
    user = request.user
    context = {
        'user':user,
    }
    return render(request, "userProfile.html", context)