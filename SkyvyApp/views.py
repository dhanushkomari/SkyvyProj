from SkyvyApp.serializers import BotDetailSerailizer
from django.shortcuts import render
from SkyvyApp.models import BotModel

from rest_framework.response import Response
from rest_framework.decorators import api_view

import time

# Create your views here.

@api_view(['GET'])
def bot_details(request, id):
    data = BotModel.objects.get(id = id)
    serializer = BotDetailSerailizer(data, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def bot_update(request, id):
    bot = BotModel.objects.get(id = id)

    print()
    print(bot.id)
    print()

    serializer = BotDetailSerailizer(instance = bot, data = request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        print('ojojfnsjodvgjosfdjgvndsfjovjd')
    # print(serializer.data)
    # newly added comment checking for git pull

    return Response(serializer.data)
 



