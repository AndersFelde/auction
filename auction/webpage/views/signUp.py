import re
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from webpage.modules.verify import Verify

verify = Verify()


def signUp(request):
    if request.user.is_authenticated:
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
                print("USER allready exists")

        remember = request.POST.get('remember', False)
        if remember:
            print(data["remember"])
            verify.logUserIn(request, data["email"], data["password1"])
            return redirect("/")
        else:
            return redirect("/logIn")

    return render(request, "webpage/signUp.html")


def validateInput(data):
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    return data["password1"] == data["password2"] and re.search(
        regex, data["email"])
