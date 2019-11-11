from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from hIncruit.models import *
from django.utils import timezone
import json
import logging
logger = logging.getLogger(__name__)
# Create your views here.

@csrf_exempt
def startQuestion(request):


    todo = '''
    1. 데이터를 받는다 ( user: user_id, clientExtra : 설문ID,문항번호,답변YN)
    2. 받은 데이터를 DB저장
    3. 설문ID와 문항번호를 이용해서 다음 설문데이터를 꺼낸다
    3-1. 마지막 설문이었다면, 챗봇에 결과보기라는 버튼을 주고 눌렀을때 설문결과페이지로 가야한다.
    4. 챗봇에 json 으로 설문전달
    5. 각 설문의 답변 버튼에 extra 로 설문id,문항번호,답변YN 값이 들어가있어야하고
    6. 각 답변은 모두 클릭시 현재 블럭ID로 재연결 해야한다.
    
    '''
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    botUserKey = ''
    try:
        botUserKey = received_json_data['userRequest']['user']['id']
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
    isFirst = 'y'
    jsonstr = ''
    logger.info(botUserKey)

    fulljson = '''{
  "version": "1.0",
  "template": {
    "outputs": [
      {
        "basicCard": {
          "title": "보물상자",
          "description": "보물상자 안에는 뭐가 있을까",
          "thumbnail": {
            "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
          },
          "profile": {
            "imageUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4BJ9LU4Ikr_EvZLmijfcjzQKMRCJ2bO3A8SVKNuQ78zu2KOqM",
            "nickname": "보물상자"
          },
          "social": {
            "like": 1238,
            "comment": 8,
            "share": 780
          },
          "buttons": [
            {
              "action": "message",
              "label": "열어보기",
              "messageText": "짜잔! 우리가 찾던 보물입니다"
            },
            {
              "action":  "webLink",
              "label": "구경하기",
              "webLinkUrl": "https://e.kakao.com/t/hello-ryan"
            }
          ]
        }
      }
    ]
  }
}'''

    #logger.info("\n\n fulljson : \n" + fulljson)
    # print(fulljson)

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