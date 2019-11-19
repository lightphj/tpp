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
def makeAnnouncement(request):
    que = ANNOUNCEMENT(category = 'R&D'
                        ,screening = '경력'
                        ,title = 'R&D부문 경력사원 모집'
                        ,content = '''R&D기획
음성인식
인공지능
IoT
차량보안'''
                        ,sub_content = '''나. 공통자격요건
  1)  해외여행 및 근무에 결격사유가 없는 자
  2)  병역필 또는 면제자
  3)  영어회화 가능자 우대

 

 

다. 전형방법(각 단계별 합격자에 한하여 개별통보)

  1)  서류전형
  2)  역량면접(PT/실무/필기/온라인 인성검사)
  3)  임원면접
  4)  신체검사 후 최종합격  


라. 접수기간 및 접수방법
  1) 접수기간 : 채용 시까지
  2) 당사 채용 홈페이지를 통해 온라인 접수
 
마. 기타사항
  1)  면접일시는 서류전형 합격자에 한하여 개별통보 예정입니다.
  2)  제출된 서류는 지원이력 위해 3년간 보관 후 삭제되며, 요청시 반환받을 수 있습니다.
  3)  국가보훈대상자 및 장애인은 관계법령에 의거 우대합니다.
  4)  입사지원서 내용이 허위로 판명될 시에는 입사가 취소될 수 있습니다.​'''
                        ,content_img = None
                        ,thumbnail = None
                        ,url = 'http://recruit.hyundai-autoever.com/hfront/RecruitManage.do?cmd=mobileRecruitShowForm&p_hgrcode=1&p_empgubun=4&p_year=2019&p_kisu=5'
                        ,create_date = '2019-11-15'
                        ,expire_date = None
                        ,last_modify_date = '2019-11-15'
                        ,del_yn = 'N'
)
    que.save()

    que1 = ANNOUNCEMENT(category = 'R&D'
                        ,screening = '경력'
                        ,title = '건설부문 경력사원 모집'
                        ,content = '''공무
시공'''
                        ,sub_content = '''나. 공통자격요건
  1)  해외여행 및 근무에 결격사유가 없는 자
  2)  병역필 또는 면제자
  3)  영어회화 가능자 우대

 

다. 전형방법(각 단계별 합격자에 한하여 개별통보)

  1)  서류전형
  2)  역량(실무)면접, 인성면접 
  3)  신체검사 후 최종합격


라. 접수기간 및 접수방법
  1) 접수기간 : 채용 시까지
  2) 당사 채용 홈페이지를 통해 온라인 접수
 
마. 기타사항
  1)  면접일시는 서류전형 합격자에 한하여 개별통보 예정입니다.
  2)  제출된 서류는 지원이력 위해 3년간 보관 후 삭제되며, 요청시 반환받을 수 있습니다.
  3)  국가보훈대상자 및 장애인은 관계법령에 의거 우대합니다.
  4)  입사지원서 내용이 허위로 판명될 시에는 입사가 취소될 수 있습니다.​ '''
                        ,content_img = None
                        ,thumbnail = None
                        ,url = 'http://recruit.hyundai-autoever.com/hfront/RecruitManage.do?cmd=mobileRecruitShowForm&p_hgrcode=1&p_empgubun=4&p_year=2019&p_kisu=6'
                        ,create_date = '2019-02-01'
                        ,expire_date = None
                        ,last_modify_date = '2019-02-01'
                        ,del_yn = 'N'
)
    que1.save()

    return JsonResponse({"test":"test"})

@csrf_exempt
def makeAnnouncementDetail(request):

    try:
        usr = ANNOUNCEMENT.objects.get(id='6')
    except(USER.DoesNotExist):
        usr = ANNOUNCEMENT(id='6')
        usr.save()

    que = ANNOUNCE_DETAIL(
                        job = '건설'
                        ,title ='시공'
                        ,content='국내 건설현장 통신공사 시공 지원 총괄/관리 (PM)'
                        ,sub_content='''- 아파트 통신공사 시공관리 총괄
                        - 발주처 협의, 대관/행정업무, 공사/공정관리, 인원관리 등'''
                        ,content_img=None
                        ,thumbnail=None
                        ,url='http://recruit.hyundai-autoever.com/hfront/RecruitManage.do?cmd=mobileRecruitShowForm&p_hgrcode=1&p_empgubun=4&p_year=2019&p_kisu=6'
                        ,rec_person_num='1'
                        ,from_date='2019-02-01'
                        ,to_date='2019-12-31'
                        ,howto=''
                        ,create_date='2019-02-01'
                        ,expire_date='2019-12-31'
                        ,last_modify_date='2019-02-01'
                        ,del_yn='N'
                        ,announcement_id=usr
)
    que.save()
    return JsonResponse({"test":"test"})


@csrf_exempt
def announcementList(request):
    #
    # 채용공고 조회 (캐로셀 return)
    #
    json_str = ((request.body).decode('utf-8'))
    #received_json_data = json.loads(json_str)
    '''category_id = ''
    try:
        category_id = received_json_data['action']['params']['category']
    except TypeError:
        logger.error("json data parising error")
    except ValueError:
        logger.error("json data parising error")
    except NameError:
        logger.error("json data parising error")
    except SyntaxError:
        logger.error("json data parising error")
    logger.info(type(received_json_data))
    print(json.dumps(received_json_data, indent=4, sort_keys=True))'''
    #tfp = place.objects.filter(category_group_code=category).order_by('distance')[:5]
    tfp = ANNOUNCEMENT.objects.filter(del_yn='N').order_by('-expire_date')
    
    #Author.objects.update(name=Trim('name'))
    isFirst = 'y'
    jsonstr = ''

    jsonrepl = ''

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
                "title": "''' + p.title + '''",
                "description": " '''+ p.content +''' ",
                "thumbnail": {
                    "imageUrl": "http://52.78.124.188:8000/static/images/irene.jpg"
                },
                "buttons": [
                    {
                        "action": "webLink",
                        "label": "상세보기",
                        "webLinkUrl": "'''+p.url+'''"
                    }
                ]
            }
        '''

    logger.info(jsonrepl)
    jsonfooter = '''
                        ]
                    }
                }
            ],
        
            "quickReplies" : [
                {
                    "label":"처음으로",
                    "action":"message",
                    "messageText":"처음으로"
                }
                ''' + jsonrepl +'''
            ]
        }   
    }'''

    logger.info("\n\n jsonfooter : \n" + jsonfooter)
    fulljson = jsonheader+jsonstr+jsonfooter

    logger.info("\n\n fulljson : \n" + fulljson)
    print(fulljson)

    dictjson = json.loads(fulljson)

    #print(dictjson)
    #places = place.objects.filter(category_group_code='01')
    return JsonResponse(dictjson
    )
