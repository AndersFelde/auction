from django.contrib.auth import logout
from django.shortcuts import redirect


def logOut(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect('/')
