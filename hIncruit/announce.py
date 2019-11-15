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
    que = ANNOUNCEMENT(category = 'ICT'
                        ,screening = '석사'
                        ,title = '상시 인재DB 등록'
                        ,content = '''인재DB에 지원서를 등록하시기 전 본인의 희망업무가 채용공고에 있는지 먼저 확인하시기 바랍니다.

진행 중인 채용공고에 등록된 지원서가 우선적으로 검토됩니다.

 


현대오토에버는 우수인재 채용을 위해 상시 채용기간이 아닌 중에도 인재DB를 운영하고 있습니다.

진행 중인 채용공고에는 해당되지 않지만 현대오토에버 입사를 희망하시는 분께서는

현대오토에버 인재DB에 등록하십시오.

 

 

인재DB에 본인 이력서를 등록해주시면 해당 이력서는 소중하게 보관되며

해당 직무에 대한 소요가 있을 시 서류전형을 실시하여 합격자에게 연락을 드립니다.

 


* 인재DB에 등록하셨더라도 진행 중인 채용공고에 자동으로 지원되지 않습니다.

* 본인이 희망하는 직무를 선택할 수 없을 시에는 현대오토에버 인사팀으로 연락 주십시오.

* 인재DB에 등록된 지원서는 반환이 불가능하니 신중하게 작성하여 주시기 바랍니다.

 

* 채용담당자 : recruit@hyundai-autoever.com/ 02-6296-4063​  '''
                        ,sub_content = '''인재DB에 지원서를 등록하시기 전 본인의 희망업무가 채용공고에 있는지 먼저 확인하시기 바랍니다.

진행 중인 채용공고에 등록된 지원서가 우선적으로 검토됩니다.

 


현대오토에버는 우수인재 채용을 위해 상시 채용기간이 아닌 중에도 인재DB를 운영하고 있습니다.

진행 중인 채용공고에는 해당되지 않지만 현대오토에버 입사를 희망하시는 분께서는

현대오토에버 인재DB에 등록하십시오.

 

 

인재DB에 본인 이력서를 등록해주시면 해당 이력서는 소중하게 보관되며

해당 직무에 대한 소요가 있을 시 서류전형을 실시하여 합격자에게 연락을 드립니다.

 


* 인재DB에 등록하셨더라도 진행 중인 채용공고에 자동으로 지원되지 않습니다.

* 본인이 희망하는 직무를 선택할 수 없을 시에는 현대오토에버 인사팀으로 연락 주십시오.

* 인재DB에 등록된 지원서는 반환이 불가능하니 신중하게 작성하여 주시기 바랍니다.

 

* 채용담당자 : recruit@hyundai-autoever.com/ 02-6296-4063​  '''
                        ,content_img = None
                        ,thumbnail = None
                        ,url = 'http://recruit.hyundai-autoever.com/hfront/RecruitManage.do?cmd=mobileRecruitShowForm&p_hgrcode=1&p_empgubun=6&p_year=2019&p_kisu=3'
                        ,create_date = '2019-11-01'
                        ,expire_date = '2020-12-31'
                        ,last_modify_date = '2019-11-01'
                        ,del_yn = 'N'
)
    que.save()