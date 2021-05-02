import re
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from webpage.modules.verify import Verify
from django.contrib import messages

verify = Verify()


def signUp(request):
    if request.user.is_authenticated:
        messages.add_message(request, messages.ERROR,
                             'Du er allerede logget inn')
        return redirect("/")

    if request.method == "POST":
        data = request.POST
        print(data)
        if validateInput(data):
            try:
                user = User.objects.create_user(username=data["email"],
                                                password=data["password1"])
                user.save()
            except:
                messages.add_message(request, messages.ERROR,
                                     'Det skjedde en feil, prøv igjen')
                return render(request, "webpage/signUp.html")

            remember = request.POST.get('remember', False)
            if remember:
                print(data["remember"])
                verify.logUserIn(request, data["email"], data["password1"])
                return redirect("/")
            else:
                messages.add_message(request, messages.INFO,
                                     f'Bruker "{data["email"]}" ble laget')
                return redirect("/logIn")

        messages.add_message(request, messages.ERROR,
                             'Passordene sammsvarte ikke')
    return render(request, "webpage/signUp.html")


def validateInput(data):
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    return data["password1"] == data["password2"] and re.search(
        regex, data["email"])
