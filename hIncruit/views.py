from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Max
from django.http import JsonResponse
from hIncruit.models import *
from django.utils import timezone
import json
import logging
logger = logging.getLogger(__name__)
# Create your views here.

@csrf_exempt
def Question(request):


    todo = '''
    1. 데이터를 받는다 ( user: user_id, clientExtra : 설문ID,문항번호,답변YN)
    2. 받은 데이터를 DB저장
    3. 설문ID와 문항번호를 이용해서 다음 설문데이터를 꺼내서 json 작성
    3-1. 마지막 설문이었다면, 챗봇에 결과보기라는 버튼을 주고 눌렀을때 설문결과페이지로 가는 json 작성
    4. 챗봇에 json 전달
    5. 각 설문의 답변 버튼에 extra 로 설문id,문항번호,답변YN 값이 들어가있어야하고
    6. 각 답변은 모두 클릭시 현재 블럭ID로 재연결 해야한다.
    
    '''

    #변수선언
    botUserKey = ''
    cur_poll_id = ''
    cur_q_id =''
    client_answer =''

    jsonstr = ''

    # payload 데이터를 받아온다.
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    try:
        botUserKey = received_json_data['userRequest']['user']['id']
        cur_poll_id = received_json_data['action']['clientExtra']['poll']
        cur_q_id_str =received_json_data['action']['clientExtra']['question']
        client_answer =received_json_data['action']['clientExtra']['answer']
    except TypeError:
        logger.error("json data parising error")
    except ValueError:
        logger.error("json data parising error")
    except NameError:
        logger.error("json data parising error")
    except SyntaxError:
        logger.error("json data parising error")
    logger.info(type(received_json_data))
    print(json.dumps(received_json_data, indent=4, sort_keys=True))
    #tfp = place.objects.filter(category_group_code=category).order_by('distance')[:5]

    try:
        usr = USER.objects.get(user_id=botUserKey)
    except(USER.DoesNotExist):
        usr = USER(user_id=botUserKey)
        usr.save()

    #받은 데이터가 있다면
    if client_answer is not None and client_answer != '':
        cur_q_id = int(cur_q_id_str)
        #받아온 데이터를 설문결과에 저장한다

        #User 객체가 없으면 User 를 먼저 만들고 insert 해야한다.




        # ANSWER 객체 생성
        ans = ANSWER(poll_id=cur_poll_id, question_id=cur_q_id, user_id=botUserKey, value=client_answer, create_date=timezone.now())

        # 새 객체 INSERT
        ans.save()
    else:
        cur_q_id = 0
        cur_poll_id_dict = QUESTION.objects.all().aggregate(Max('poll_id'))
        cur_poll_id = int(cur_poll_id_dict['poll_id__max'])
        print(cur_poll_id)
        print(type(cur_poll_id))

    # 전체 문항수를 가져와서 문항수=번호 이면 basicCard 로 설문이 끝났음을 알리고, endQuestion block 으로 연결하는 버튼을 제공하는 json 작성
    len = QUESTION.objects.filter(poll_id = cur_poll_id).count()
    if len <= cur_q_id:
        #설문 끝났습니다
        jsonstr='''
            {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "basicCard": {
                                "title": " 모든 문항 완료 ",
                                "description": "모든 문항에 응답해 주셨습니다.",
                                "buttons": [
                                    {
                                        "action": "block",
                                        "messageText": "결과보기",
                                        "label": "결과보기",
                                        "blockId": "blockId"
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
        '''
    else:
        #설문 데이터를 가져온다.

        q = QUESTION.objects.get(poll_id = cur_poll_id, question_id = cur_q_id+1)

        jsonstr = '''{
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "basicCard": {
                            "title": "Q.'''+ str(q.question_id) + '''/''' + str(len) +'''",
                            "description": "''' + q.subject + '''",
                            "buttons": [    
                                {
                                  "action": "block",
                                  "label": "Y",
                                  "messageText": "Y",
                                  "blockId": "5dc910428192ac0001c5e495",
                                  "extra": {
                                    "poll" : "''' + str(q.poll_id) + '''",
                                    "question" : "''' + str(q.question_id) + '''",
                                    "answer" : "Y"
                                  }
                                },
                                {
                                  "action": "block",
                                  "label": "N",
                                  "messageText": "N",
                                  "blockId": "5dc910428192ac0001c5e495",
                                  "extra": {
                                    "poll" : "''' + str(q.poll_id) + '''",
                                    "question" : "''' + str(q.question_id) + '''",
                                    "answer" : "N"
                                  }
                                }
                            ]
                        }
                    }
                ]
            }
        }'''






    logger.info(botUserKey)
    #챗봇에 json 전달
    fulljson = jsonstr

    #logger.info("\n\n fulljson : \n" + fulljson)
    print(fulljson)

    dictjson = json.loads(fulljson)

    # print(dictjson)
    # places = place.objects.filter(category_group_code='01')
    return JsonResponse(dictjson
                        )


def endQuestion(request):
    todo = '''
    1. 유저 데이터를 받는다 ( user: user_id)
    2. userid 로 가장 최근의 설문조사 결과를 토대로 맞는 직군을 선정한다. (아니면 clientExtra 로 설문번호도 받아올까?)
    2-1. 섬룬조사 결과를 iter 하면서 해당 문항과 YN 의 답변이 일치하는 question_category 를 찾아서 +1 한다 
    2-1-1. 그러려면 dict 로 먼저 전체직군,값(초기값 0) 을 가져와야한다.
    2-1. iter를 다돌면, 가장 높은 점수를 찾고, 동일점수가 여러개일시 '~~~~' 의방법으로 order 해서 한줄만 가져온다.
    3. 가져온 직무와 그 내용을 뿌려주고, 다시 설문하기와 처음으로 돌아가기 quickRepl 을 준다.
    '''


def makeQuestion(request):
    que = QUESTION(poll_id=1, question_id=1, subject='설문1 질문1 입니다')
    que.save()

    return JsonResponse({"test":"test"})
