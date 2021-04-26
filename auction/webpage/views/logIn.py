from django.shortcuts import render, redirect
from django.contrib import messages
from webpage.modules.verify import Verify

verify = Verify()


def logIn(request):
    if request.user.is_authenticated:
        messages.add_message(request, messages.INFO,
                             'Du er allerede logget inn')
        return redirect("/")

    if request.method == "POST":
        data = request.POST
        if "email" in data or "password" in data:
            if verify.logUserIn(request, data["email"], data["password"]):
                return redirect('/')

            messages.add_message(request, messages.INFO,
                                 'Passord eller brukernavn var feil')
            return render(request,
                          "webpage/logIn.html",
                          context={"email": data["email"]})

    return render(request, "webpage/logIn.html")
