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
                        ,create_date = '2019-02-01
                        ,expire_date = None
                        ,last_modify_date = '2019-02-01'
                        ,del_yn = 'N'
)
    que1.save()

    return JsonResponse({"test":"test"})
