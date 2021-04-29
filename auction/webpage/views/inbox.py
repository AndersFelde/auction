from django.shortcuts import render, redirect
from webpage.modules.database import Database
from django.contrib import messages

db = Database()


def inbox(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.INFO,
                             'Du må være logget inn for å se inbox')
        return redirect("/logIn")

    notifications = db.getNotifications(request.user.id)
    return render(request,
                  "webpage/inbox.html",
                  context={"notifications": notifications})
