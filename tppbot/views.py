from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from tppbot.models import *
from tppbot.forms import *
from django.utils import timezone
import json

import logging
import logging.config
import os

with open('tppbot/logging.json', 'rt') as f:
    config = json.load(f)

logging.config.dictConfig(config)

logger = logging.getLogger()




@csrf_exempt
def keyboard(request):
    s = ""
    for f in Store.objects.all():
        s += f.storename + '\n'
    print(s)
    return JsonResponse({
        'name': s
    })


@csrf_exempt
def answer(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    # print(json.dumps(received_json_data, indent=4, sort_keys=True))

    action = received_json_data['action']
    params = action['params']
    datacontent = params['content']

    if datacontent == '버튼1':
        button1 = "버튼1을 누르셨습니다."

        return JsonResponse({
            'message': {
                'text': button1
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['버튼1', '버튼2']
            }

        })

    elif datacontent == '버튼2':
        button2 = "버튼2을 누르셨습니다."

        return JsonResponse({
            'message': {
                'text': button2
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['버튼1', '버튼2']
            }

        })


@csrf_exempt
def todaysmenu(request):
    return JsonResponse({
        "version": "2.0",
        "data": {
            "shopName": "마부육전",
            "bestMenu": "육전냉면"
        }
    })


def showUser(request):
    template_name = 'tppbot/User.html'
    form_class = UserForm
    model = User
    success_url = ''

    users = User.objects.filter(create_date__lte=timezone.now()).order_by('create_date')
    return render(request, template_name, {'users': users})


def addUser(request):
    template_name = 'tppbot/addUser.html'
    form_class = UserForm
    model = User
    success_url = ''
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.insert()
            return redirect('showUser')
    else:
        form = UserForm()
        return render(request, template_name, {'form': form})


@csrf_exempt
def topFivePlace(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    category = ''
    try:
        category = received_json_data['action']['params']['category']
    except TypeError:
        logger.error("json data parising error")
    except ValueError:
        logger.error("json data parising error")
    except NameError:
        logger.error("json data parising error")
    except SyntaxError:
        logger.error("json data parising error")
    #logger.info(type(received_json_data))
    #print(json.dumps(received_json_data, indent=4, sort_keys=True))
    tfp = place.objects.filter(category_group_code=category)
    isFirst = 'y'
    jsonstr = ''

    jsonrepl = ''

    replK = ''',{
                    "messageTex":"한식",
                    "action":"message",
                    "messageText":"한식"
                }'''
    replW = ''',{
                    "messageTex":"양식",
                    "action":"message",
                    "messageText":"양식"
                }'''
    replC = ''',{
                    "messageTex":"중식",
                    "action":"message",
                    "messageText":"중식"
                }'''
    logger.info(category)
    logger.info(type(category))
    if category == '01' :
        jsonrepl = replK+replC
    elif category == '02' :
        jsonrepl = replK+replW
    else:
        jsonrepl = replC+replW


    jsonheader = '''{

        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "carousel": {
                        "type": "basicCard",
                        "items": [ '''

    for p in tfp:
        if isFirst != 'y':
            jsonstr = jsonstr + ','

        isFirst = 'n'

        jsonstr = jsonstr + '''
            {
                "title": "''' + p.place_name + '''",
                "description": " '''+ p.phone +''' ",
                "thumbnail": {
                    "imageUrl": "http://52.78.124.188:8000/static/images/irene.jpg"
                },
                "buttons": [
                    {
                        "action": "webLink",
                        "label": "''' + p.road_address_name +'''",
                        "webLinkUrl": "'''+p.place_url+'''"
                    }
                ]
            }
        '''

    logger.info(jsonrepl)
    jsonfooter = '''
                        ]
                    }
                }
            ]
        }, {
            "quickReplies" : [
                {
                    "messageTex":"처음으로",
                    "action":"message",
                    "messageText":"처음으로"
                }
                ''' + jsonrepl +'''
            ]
        }   

    }'''


    fulljson = jsonheader+jsonstr+jsonfooter

    #print(fulljson)

    dictjson = json.loads(fulljson)

    #print(dictjson)
    #places = place.objects.filter(category_group_code='01')
    return JsonResponse(dictjson
    )



@csrf_exempt
def list(request):

    return JsonResponse(
        {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "basicCard": {
                            "title": "어떤 종류의 음식점을 갈까?",
                            "description": "한식/양식/중식 택1",
                            "thumbnail": {
                                "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
                            },
                            "buttons": [
                                {
                                    "action": "message",
                                    "label": "한식",
                                    "messageText": "한식"
                                },
                                {
                                    "action": "message",
                                    "label": "중식",
                                    "messageText": "중식"
                                },{
                                    "action": "message",
                                    "label": "양식",
                                    "messageText": "양식"
                                }
                            ]
                        }
                    }
                ]
            }
        }
    )