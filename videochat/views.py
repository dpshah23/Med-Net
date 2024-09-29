from django.shortcuts import render
from django.http import JsonResponse
import random
import time
from agora_token_builder import RtcTokenBuilder
from .models import RoomMember
import json
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
import os
from django.urls import reverse
from django.utils.http import urlencode


# Create your views here.

def lobby(request):
    return render(request, 'base/lobby.html')

def room(request):
    return render(request, 'base/room.html')

load_dotenv()

def getToken(request):
    appId = os.getenv("APP_ID_AGORA")
    appCertificate = os.getenv("APP_CERTIFICATE_AGORA")
    channelName = request.GET.get('channel')
    uid = random.randint(1, 230)
    expirationTimeInSeconds = 3600
    currentTimeStamp = int(time.time())
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1

    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)
    join_url = f"http://127.0.0.0:8000/room/?token={token}&room={channelName}&uid={uid}"

    return JsonResponse({'join_url': join_url}, safe=False)


@csrf_exempt
def createMember(request):
    data = json.loads(request.body)
    member, created = RoomMember.objects.get_or_create(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )

    return JsonResponse({'name':data['name']}, safe=False)


def getMember(request):
    uid = request.GET.get('UID')
    room_name = request.GET.get('room_name')

    member = RoomMember.objects.get(
        uid=uid,
        room_name=room_name,
    )
    name = member.name
    return JsonResponse({'name':member.name}, safe=False)

@csrf_exempt
def deleteMember(request):
    data = json.loads(request.body)
    print(data)
    member = RoomMember.objects.filter(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )
    print("member : ",member)
    if member.exists():
        member.delete()
        return JsonResponse('Member deleted', safe=False)
    else:
        return JsonResponse({'error': 'Member does not exist'}, status=404, safe=False)

