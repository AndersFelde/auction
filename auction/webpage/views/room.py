from django.shortcuts import render


#  from webpage.models import TestModal
def room(request, room_name):
    print(room_name)
    return render(request, 'webpage/room.html', {'room_name': room_name})
