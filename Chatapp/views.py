import random
import string
from django.shortcuts import render, redirect
from .models import *
from auth1.models import *


def CreateRoom(request):

    if request.method == 'POST':
        email = request.SESSION.get('email')
        username = User.objects.get(email=email).name
        room = ''.join(random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits) for _ in range(8))
        role = request.SESSION.get('role')
        try:
            get_room = Room.objects.get(room_name=room)
            return redirect('room', room_name=room, username=username)

        except Room.DoesNotExist:
            new_room = Room(room_name = room)
            new_room.save()
            if (role == doctor):
                new = joined(new_room = room , username = doctor)
                new.save()
            else :
                new = joined(new_room = room , username = patient)
                new.save()
            return redirect('room', room_name=room, username=username)

    return render(request, 'list.html')

def MessageView(request, room_name, username):

    get_room = Room.objects.get(room_name=room_name)

    if request.method == 'POST':
        message = request.POST['message']

        # print(message)

        new_message = Message(room=get_room, sender=username, message=message)
        new_message.save()

    get_messages= Message.objects.filter(room=get_room)
    
    context = {
        "messages": get_messages,
        "user": username,
        "room_name": room_name,
    }
    return render(request, 'message.html', context)


def list_of_rooms(request):
    email = request.SESSION.get('email')
    username = User.objects.get(email=email).name 
    role = request.SESSION.get('role')
    if (role == doctor):
        rooms = joined.objects.filter(username = doctor)
        return redirect()
    
    elif (role == patient):
        rooms = joined.objects.filter(username = patient)
        return redirect()
  