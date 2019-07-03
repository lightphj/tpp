from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from tppbot.models import Store, User
import json
 
 
@csrf_exempt 
def keyboard(request):
    s = ""
    for f in Store.objects.all():
        s += f.storename + '\n'
    print(s)
    return JsonResponse({
        'name':s
    })
 
@csrf_exempt
def answer(request):
 
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    #print(json.dumps(received_json_data, indent=4, sort_keys=True))
    
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
                    'type':'buttons',
                    'buttons':['버튼1','버튼2']
                }
 
            })
 
    elif datacontent == '버튼2':
        button2 = "버튼2을 누르셨습니다."
 
        return JsonResponse({
                'message': {
                    'text': button2
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['버튼1','버튼2']
                }
 
            })
      
@csrf_exempt
def todaysmenu(request):

    return JsonResponse({
        "version": "2.0",
        "data" : {
            "shopName" : "마부육전",
            "bestMenu" : "육전냉면"
        }
    })
