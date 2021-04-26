from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages


def logOut(request):
    if request.user.is_authenticated:
        messages.add_message(request, messages.INFO, 'Logget ut')
        logout(request)

    return redirect('/')
