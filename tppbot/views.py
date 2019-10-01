from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from tppbot.models import *
from tppbot.forms import *
from django.utils import timezone
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


def list(request):
    return JsonResponse({
        "version": "2.0",
        "template": {
            "outputs" : [
                {
                    "simpleText": {
                        "text" : "양식점1 "
                    }
                }
            ]
        }
    })