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
    que = ANNOUNCEMENT(category = '4'
                        ,screening = '경력'
                        ,title = 'ICT부문 경력사원 모집'
                        ,content = '모빌리티/커넥티비티, 시스템 개발/운영, 보안, 웹/서버개발, 프로젝트관리'
                        ,sub_content = '.'
                        ,content_img = None
                        ,thumbnail = None
                        ,url = 'http://recruit.hyundai-autoever.com/hfront/RecruitManage.do?cmd=mobileRecruitShowForm&p_hgrcode=1&p_empgubun=4&p_year=2019&p_kisu=12'
                        ,create_date = '2019-06-19'
                        ,expire_date = None
                        ,last_modify_date = '2019-06-19'
                        ,del_yn = 'N'
)
    que.save()

    que2 = ANNOUNCEMENT(category = '6'
                        ,screening = '경력'
                        ,title = '빅데이터부문 경력사원 모집'
                        ,content = '데이터 엔지니어링'
                        ,sub_content = '.'
                        ,content_img = None
                        ,thumbnail = None
                        ,url = 'http://recruit.hyundai-autoever.com/hfront/RecruitManage.do?cmd=mobileRecruitShowForm&p_hgrcode=1&p_empgubun=4&p_year=2019&p_kisu=12'
                        ,create_date = '2019-06-19'
                        ,expire_date = None
                        ,last_modify_date = '2019-06-19'
                        ,del_yn = 'N'
)
    que2.save()

    que3 = ANNOUNCEMENT(category = '7'
                        ,screening = '경력'
                        ,title = '스마트교통부문 경력사원 모집'
                        ,content = 'C-ITS'
                        ,sub_content = '.'
                        ,content_img = None
                        ,thumbnail = None
                        ,url = 'http://recruit.hyundai-autoever.com/hfront/RecruitManage.do?cmd=mobileRecruitShowForm&p_hgrcode=1&p_empgubun=4&p_year=2019&p_kisu=12'
                        ,create_date = '2019-06-19'
                        ,expire_date = None
                        ,last_modify_date = '2019-06-19'
                        ,del_yn = 'N'
)
    que3.save()

    que4 = ANNOUNCEMENT(category = '5'
                        ,screening = '경력'
                        ,title = '경영지원부문 경력사원 모집'
                        ,content = 'IR'
                        ,sub_content = '.'
                        ,content_img = None
                        ,thumbnail = None
                        ,url = 'http://recruit.hyundai-autoever.com/hfront/RecruitManage.do?cmd=mobileRecruitShowForm&p_hgrcode=1&p_empgubun=4&p_year=2019&p_kisu=12'
                        ,create_date = '2019-06-19'
                        ,expire_date = None
                        ,last_modify_date = '2019-06-19'
                        ,del_yn = 'N'
)
    que4.save()

    return JsonResponse({"result":"success"})

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

        imageUrl_bind =''

        if p.category == '2':
            imageUrl_bind = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTaM5-9OLMcs6djsGdpgwMPO6Q656BLdgrYp_bI8xYEp118bl8M&s'
            #imageUrl_bind = 'http://52.78.124.188:8000/static/images/irene.jpg'
        elif p.category == '3':
            #imageUrl_bind = 'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxATEBATEw8VEhQXFRUXFRUWFQ8QFRUVFRUWFhUYGBUYHSggGBslHRUVITIhJSkrLi4uFx8zODMtNygtLisBCgoKBQUFDgUFDisZExkrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrK//AABEIAOEA4QMBIgACEQEDEQH/xAAcAAEAAwADAQEAAAAAAAAAAAAAAQcIAgUGBAP/xABREAABAwIDBQMFCA4JAwUBAAABAAIDBBEFITEHEkFhcQYTUSKBk7HSCDJUVXKRkvEUFyUzNUJSU4KDobPR0xUjJDRDYmR0shhjtHOUosHwRf/EABQBAQAAAAAAAAAAAAAAAAAAAAD/xAAUEQEAAAAAAAAAAAAAAAAAAAAA/9oADAMBAAIRAxEAPwC70v4IfBRyH1IJJ4BCeHFRpkNU05lBJNuZQmyjTmU0zOqCb21S/EqOZ+pOZQSDxOSA/Mo16Jr09aA6QAEk2aBck5Cw1PIKlcf29Bszm0tGJI2kgSSPc0vtxDAPJB4XN+Q0Vndu3H+i8Stl/ZKnP9S9Y8QXGdv1V8Ah+nKn2/qr4BD9OVU4iC4/t/VXwCH6cqDb9VfAIfpyqnEQXZh23+TvB3+Ht7v8YxSO3wPEBws7pcdVdmHV8c0Mc0b9+ORrXscOLXC4y4HksTrU+xM/cKiJP5+3/uZUHub8SgPEqOZTXM6IJBQG/RRr09aa9PWgkG/RL+CjXIJyH1IJJ4BCeAUaZBNOqCSfnU3XHTmVIFtdUEqVClBxJ4BRpkNVJPhqo05lA05lNOZTTmU0zOqBpmdU5n6k5n6k5lA5lNeiDPoqs2ibYYKUvgow2onFw5+sMZ6j744eAyHE5WQWJjeN01LEZamdkMY4uObiM7NaM3HkASql7R7dAXiKhp7guDe+myyJAu2Jpv0JPmVM43jdTVymWpnfNIeLjkB4NaMmjkAAvlovvsfy2/8AIINedvT9ysSA+B1P7l6x6th9vT9ysSA+CVP7l6x4gIiICIiAtT7ER9wqLrP/AOTKssLU2xIfcOi6z/8AkyoPJUW28RVU0FZTXYyaRjZYdbNeWtLo3HPIZkHzK1MBx+krY+8pqhkzMr7p8ppPB7D5TTyICyL2nP8Abqz/AHE37xy+fC8TnppWywTPhkGjmOLTa4Nj4g2zByPFBtTXp601yCqLZ9tmjn3Kev3YJTk2ceTE/wAA8f4bufvdfe6K3QfD50DkPqTTIJpkE06oGnVNOZTTmU0zOqBpmdVIHEqOZUgcSglSoupQcSbdVGnMqSbKNMzqgaZnVOZ+pOZ+pOZQB4lQ94ALnENaASSSAABmSTwCkC/RZ+207STO99BSP/qGm08jT9+cNWNI/wAMHX8o8hmEbVtrD6gvpKGQsgFxJM27XTcC1h1bHz1d01qJEQF+9F99j+W3/kF+C5wybrmu8CD8xug2B29P3KxIf6Sp/cvWPFsrFIWVuHzMikG7VU72sk98LTRkNdbiPKBWb6jZFjjXFoog8A2DmzU267mN54NuoCDwqL252S478APpqP8AmIdkuO/AD6ej/mIPEIvb/alx239wPp6P+Yg2S478Xn01H/MQeIWptiQ+4VF4Xn/8mVUgzZJjvwDz99SfzFoPsFgzsPwunp5pG3ibI6Rw96N575XC54N3rX42QZY7T/36s/3E37xy6xfZi9SJaieUDJ8sjwOTnlw9a+NAVnbL9qstFuU1UTLSXAa7Nz6ceLRq5g/J1HDwNYog23S1LHsY+N4ka8BzXNIc1zSLhwI1C/TTmVm3Y9tFNDKKWofekkdkSf7u9x98PBhPvhw99430k0i173vpbO/hZA0zOqcynMpzKBzKkZ5qNczopGfT1oOV0REHE5ZqOZ+pSfEqOZQOZTXomvRfjWVcccb5JXiONgLnOcQ1oA1JPAIK422dtH01P9iU+9387TvObe8UJyJuNHOzA5BxyyWcxSyfm3fRctbnt1hJ/wD6dLb/ANaL+KHt1hGgxOlH66L+KDIz4XjMscOoIX5rX7e2mEus0YjSG/jND/8AZzK/HGOxWE1zLvpIX72ksW7G/r3kdr9DcIMjIrR2gbHaija6alc6qgGbmkDvo2gZkgZPbzABF9LAlVcgsfZ1tXnw9gglj+yKYe9G9uyRXzIY45FuvknxyIVgt29Yb8Fqr/Jp/wCYs7og0QNvOG/Bav6NP/MT7fWG3/utX9Gn/mLO6INEHb1ht/7rV/Rp/wCYh29Yb8Fq/o0/8xZ3RBoh23rDfgtX9Gn/AJi8LtD2uz10TqeniNNTuyeS7ellb+SSMmN8QL3trYkKsUQERWJs/wBlNVXhs0xNNTHNriLySj/ttOjf8xy0sCgrtc2ROdo0kcgT6lrHBNn+EULAWUkbnNzMs27K+9td5+TP0QAvsf2wwmIlpxGkaRkQJocuVgckGRTSyfm3fRcr72Fdsnvj/o+p3g+Nv9me4Eb0Y1jz4tGn+W4/FXvB25wjU4nS+mi/ig7c4RqcTpeX9dF/FB6LmU1zOi+XDMSgqYxLDMyWO5Acxwc0lpscwvq16etA16etTe/RRr09am/gg5IospQcSOJUa9FJHzKNenrQNenrVPe6J7SblPBQsdYynvJbW+9RnyGnkX5/q1cOvRZM2pY39l4tVyXuxjzDHxG5F5FxyJDnfpIPJoiIC7bs92krKKQSU1Q+I3uWg3Y7k9h8l3nC6lEGodmG0mLEmGORoiq2i7mD3sgGro759WnTmq8247P207vs+mYGwvdaeNosI5HHJ7Rwa45EcDbxyqzCsRlp54p4XFkkbg9pHiPHxB0I4gkLWtHLBimFtc4f1VVBZzddwuFnAHxa4HPxagx+i+jEKR8MssLxZ8b3xvt+Uxxa79oK+dAX0UNDNM/chhfM+192Nj5HW8d1oJ4ruOw3ZiTEK2KmYd0G7pH693E33zuuYA5uC1DRUeHYVSWb3dLA22+9xDS92l3POb3H5+AQZSr+zddA3fmop4m/lvila0fpEWXVrYOCdssNrXGKnq45XWN2eU1xaNbNeAXDoqi237PYadv2dSRiOPeDZ4mgBjC7Jr2j8UE2aQOJHNBTaIuTGFxAAuSQABmSToAgsrYx2CFdMamoZvU0LgAw6TS67p8WNFifG4GeauDaJ2+p8KhaN0S1Dwe6hGQAGW+8j3rBoBqTkNCR2eBUMOF4XGx1g2ngL5XD8ZzWl8rvO7ePnCyn2lxyatqpqmU3dI4m17hjfxWDk0WHmQfR2m7W11fIXVNQ54vcRg7sTPANjGQt46+JK6REQEREFxe527Q7lRPQvd5Mo72IZW71g8sDm5gB/VK/denrWMuzeKupKumqW3vFI15A4tB8tvnbcedbLjkD2gtN2kAgjQgi4t5kHLXIaKb8Ao5D6lPIIJspUKUHEi/RRr0UnPoo5BB1vafEvseiq5x/hQyPHymsJaB57LGZPE/WtSbbaru8EqwDYuMTPDIysLh5wCPOstICIiAiIgLSnufKovwgtOkVRKwdC1knrkKzWtFe5yH3MqP94/8AcwIKk2uQhmNYgBxka7zvjY8/tcV5Be02yn7uV/yov3ES8Wguv3NdEC/EJTa4bDGPGzi9zvN5LfmXye6Pr3mrpIN4922EyBvDfe9zSSOOTAPOfFdr7mq/d4j8qD1SLofdG2/pKm/2rf3sqCr6KrkhkZLG8skY4OY4ahzTcFax7fgSYLX7zQb0kj7cAQzfB8xA+ZZHWue2eWCVv+yl/clBkZd72EgEmKYew6Gph/ZI02/YuiXo9nB+6+G/7mL/AJBBoTbVUOjwSsINi/umX5OlZvDzi486ywtQbdB9xKi/5cP71qy+gIiICIiAtZ7KsTNRg9A7i2PunXzN4XGL5yGg+dZMWjPc7VZdhk0d77lS+3Jro43f8t8+dBafIKRllxUaZDVSMuqDkihSg/OaQNDi5wa0AlziQA0AXJJOnVVpjW27C4XmOJs1TbIvjaxsdwbGxeQXdbW8CV1Xuiu0EkcNNRscWtm3ny2Nt5jC0MZ0LiSfkhUCgtfaZtSpsRoRTRU8sZ71jy55jsWtDrjySTe5HzKqERAREQEREBWhsu2mU2GUksEtPLIXTulBYY7WMcbbHeIz8g/OqvRB3/bzHWVuIVNUxjmNkLCGutvDdjYw3tlq0roERBYuyjaDBhbKoSwSSd66Mgs3MtwPBvvEflBddtQ7XwYnVRTRRyRNZCIyH7hJIe918j/mXi0QciB4n5h/FXVjm2Wjnw+opW0s4fJTviDiYt0OdGWAmzr2VJogLteyuKNpa6lqHNLmxSskc1tt4hpuQL5XXVIgt3aJtYpcQoJaWOmmY9zoyHPMe6Nx4cdDfgqiREBERAREQFZGyjaNDhcdUyWCSUSOY5u5uC26HB194j/L8yrdEGjMO264Y94bJDUQg6vLWSNHUMcXW6AqzaCsiljZLFI2Rjxdr2kOa4ciFiZXN7nPHpBUVFE5xMRjMzATfce1zWu3Rw3g8E/IHigvtSoUoKX90dgb3xUtW0XbFvRy2/FEhaY3HlvAjq5qoVbcq4GPY+N7Gva8FrmOAc1zSLEOB1FlVmNbCqCR5dDUS09zfu7NmYOTb2cB1JQZ2RXwdgEPxk/0LPbT/p/ht+En+hZ7aCh0V8f9P8Nvwk8fqWe2g9z/AA/GT/Qs9tBQ6K+G7AIfjJ/oWe2jdgEPxk/0LPbQUOivgbAIfjJ/oWe2n2gIb/hJ/oWe2godFfB2AQ3/AAk/0LPbQ7AIfjJ/oWe2godFfDtgEPxk/wBCz20OwCH4yf6FntoKHRXwfc/w2/CT/Qs9tP8Ap/ht+Enj9Sz20FDor4Huf4fjJ/oWe2jfc/w/GUnoWe2godFfDdgEPxk/0LPbQbAIfjJ/oWe2godFfH2gIb/hJ/oWe2h2AQ3/AAk/0LPbQUOivg7AIfjJ/oWe2jtgEPxk/wBCz20FDor4OwCH4yf6FntodgENvwk/0LPbQUOrn9zlgUnf1Na5pEbY+5YTo97nNc+3yQwD9Nd9hewahY4Onqppmg33AGQg8nEXNuhCtPDqGKGJkUUbYomCzGNFgB0/b50H03UqLqUHEm3VflUvLWPdxDXEdQCQv1OWa4SxgtcHcQR0BFkGbft34v4U/one0h234v4U/one0vlxvY7jEDnd3A2pYL2fE9gJHC8biHA24C/VeMxLB6qnNp6aWE3t/WRyR58i4Z6IPenbfi/hT+id7SO234v/AKf0TvaVaIgss7b8X/0/one0h234v/p/RO9pVoiC1cK224kZ4BN3AiMjBIRG4ERlw3yDvZG11oq/ALEC1hsp7SCtwunfvb0sYEMvE78YADj8pu67zlB6/TqmnMppzKaZnVA0zOqcynMpzKBzKa5nRNczomvT1oGvT1pr09aa9PWmuQ0QNchoqB7WbZMQhrquKn7nuY5Xxs3oy4kMO6TfezuQT51b/bztE2gw+onuA5rd2IHjK/JgtxzzPJpWQCSSSTfnqSUFlDbfi/hT+id7SN234v4U/one0q0RBZY234v4U/one0g234v4U/one0q0RBZf278XvpT+id7SHbfi99Kf0TvaVc09O+RwbGxz3H8VrS4nzBeqwnZljE9t2gkY02u6XdgAHiQ8h1ugKDTPZDEJKmgo6iW2/JCx7rCzd5zbmw4BdwM+nrXV9mMLNNRUtO5wd3UMcZcLgOLWgEjlddpe/T1oOSIiDifEqOZUkcSo1zOiBrmdFD2BwIIBb4EAg9R4KdenrTXp60FDe6D7MwwikqoII4muc+KXu2NjDnny2OIaLEkCXPXIKmVr7aBgH2dh1TTNA3y3ejJyAlZ5TBfhcixPgSshvaQSHAgg2IORBGoIQcUREBe12VdtThtZvPuaaUBk4GdgD5EgHEtucvBzuNl4pEG3KeZjmNka4Pa4BzXNIcHNIuC0jUELnzKzRsu2nyYeRTzh0tITlxfATqWeLeJb5xncHReEYpBUxNngmbLG7RzTccweId4g5hB9nMprmdE1zOia9PWga9PWmvT1pr09aa5DRA1yGih7wAcwABck5AAa5r8MQr4oI3SSyNijaLue8hrWjqePJZ82o7VnVjXUtHvR0uj5Ddr5x4W1bHy1PG2YQdbth7cDEKoRQu/ssBIYQTaWTR0lvDg3lc/jEKvURAREQFZOwzszDWV0r54WywwxXLXgOaZHndYC05HISH9FVstQ7E+zhpMLje8WkqD3zvENcAIgf0bG3AuKD21BQQwtDYoY4WDRsbGRt+ZoAX0a9PWmvT1pr09aBr09am/hoo1yGim/AIOVkUWUoOJCjXp61JF+ijXp60DXp601yCa5BOQ+pA5D6llzbXh9NDi84gcDvtbJK0WtHM+5c3zjdf1eVf20LtZHhtDJNkZD5ELD+NKRlfkPfHkOYWSqupfLI+SRxe97i57jq5zjck8ySg/JERAREQF2vZ/tHV0UneUtQ6JxtvAZsdbQOYfJd5wuqRBdeBbe3gBtZRh/i+B26T1jfl/8h0XrqbbVgzwN580XiHwuJ6eQXLMyINNVm2rBmjyZJpOTIXDzeXuryeO7fDultHRbp4Pnde36pntKkUQdz2j7UVtc/fqqh0lvesybG35LBZo11tfmumREBERAREQeg7A4bBUYlRw1DwyJ8g3r5B1gS2P9NwDf0lr9rdMrAaDT/wDBYha4ggg2IzBGRBGllqjZP2y/pKib3jv7RDusnGV3ZeRJbwcAb8w5B7bXp601yGia5DROQQOQU8go5BTpkglSoUoOJF+ijXIKT4KOQ+pA5D6k0yCaZBNOqDMe3PFaiXFZIpQWxwBrYW55te1rnP5lx4+DQOCrxaw2jdg4MTgsbMqWA9zNbz7j7asP7NRxBy7jWEz0s8kE8ZjkYbOaf2EHiDqCEHwoiICIiAiIgIiICIiAiIgIiICIiAvV7MMZnpcTpXQgu7x7Ynxj/EjkcA4ebJwPi0LzVHSySyMjjYXyPIaxjQS5zjkAAtK7K9m7MPYJpg19Y9vlOyc2Bp1Yw/leLvMMtQsTkE5BOQTTIaoGmQ1UjLqo05lSMuqCVKhSg4k8Ao0yCkngFGnVA06ppzKacymmZ1QNMzqvIbRuwcGJweVaOoYD3MttOO4+2rCfmvccQfX8ynMoMXY1hM9LPJBPGY5GGzgf2EHi0jMFfGxpJDWgkk2AGZJOgAWs+3fYSlxSNve3ilZ97mYG77Rxa4H3zeNvmIzXzdhtm1Dh1ntb30/5+QDeHyG6RjpmfFBWHYDYvNPuT1+9BFkRCMpnjXy/zQ0y99r73Vdr2w2GAl0mHSgf9iUm36uXXzO+krt16etNchogxljWAVdI/cqaaSF17DeaQ11vyX+9d5iV1q23U07JGmN7GvaffNc1r2kcwciqN28djKKmgp6mmpmwky93II95rSHMc5h3PetzadANUFLIiICIiAvuwjB6mqf3dPTyTOyuGNLrX4uOjRzOSsTYR2UpayeqkqYRNHC2Pda7e3N95dmQMnWDDkbjNaGoaKKJgZFEyKMaMY1sbR+iMkFH9j9hcrt2TEJu7bke5iIc88nye9b0bfqF+3brYlYOmw05caZ7rnIf4UjtfkuPjnwV469PWmvT1oMS1NM+J7mSMdG9ps5j2ljmnwLTmCpo6WSWRkcbC+R7g1jGglznHIABa07Zdh6HEmWmj3ZALMnZZsjfAX/Gb/lNx0Oa6zsDs0pMNc6RrzUTnLvXta3u2nUMaL7pPE3v0QfJsr2bsw9gmmDX1jx5TsnNgadWMP5Xi7zDLWw+QTkE0yGqBpkNU05lNOZTTqgadVIHEqNMypA4lBKlEQcSfnUacyuRUAWz4oI0zOqcypA4lAOJQRzKa5nRTa+qWv09aCNenrTXp61Jz6IfBBGuQ0TkPqUnwCcggjkF4vbJh3fYLWAC7mBso/Vva55+hvr2ummq+bEqJs0E0L82yxvjd0e0tP7CgxQisqp2I4u1zg0QPaDk4S7u8OBsRcL8zsUxn83D6Zv8EFcorG+0pjP5uH0zf4LkzYnjOXkQDmZhYfMEFj+55w3u8LklI+/TvI+RGGsF/wBISK0NenrXT9j8CFFQ01LvB3dMsSBYOeSXPNvAuc4ruTn09aCNenrTXIaKT4cEPgEEcgnIKeQTTRBGmQ1TTmVNrcygFuqCNOqaZlSBxKAcSgjmfqUjPMpa+ZTXogm6lEQQilEEIVKIBREQFAUoggIpRAUKUQQilEEFCpRAREQAoClEEIpRBCKUQQpREEFSiIIREQf/2Q=='
            imageUrl_bind = 'https://cdn4.vectorstock.com/i/1000x1000/71/83/office-building-icon-with-outline-style-vector-21947183.jpg'
        elif p.category == '4':
            #imageUrl_bind = 'data:image/jpeg;base64,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'
            imageUrl_bind = 'https://image.shutterstock.com/image-vector/ict-cloud-computing-chips-tech-260nw-1014765394.jpg'
        elif p.category == '5':
            imageUrl_bind = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTwzNHw5asNYS7mC3UYAxlhWJRM1OFod3GQdoXhggbAEBGoIFwc1Q&s'                    
        elif p.category == '6':
            #imageUrl_bind = 'data:image/png;base64,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'
            imageUrl_bind = 'https://zdnet3.cbsistatic.com/hub/i/r/2018/01/01/00a8ffa1-ff8e-49c6-9a3c-44e622af1824/resize/770xauto/24b0310cdf6050ae4318ea623afb07c4/big-data-pix.jpg'
        elif p.category == '7':
            imageUrl_bind = 'https://img.pngtube.com/myfile/small/49-492768_trains-are-being-operated-in-a-very-complex.png'
        else:
            imageUrl_bind = 'http://52.78.124.188:8000/static/images/irene.jpg'

        jsonstr = jsonstr + '''
            {
                "title": "''' + p.title + '''",
                "description": "'''+ p.content +'''",
                "thumbnail": {
                    "imageUrl": "'''+ imageUrl_bind +'''",
                    "fixedRatio": "true"
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

    #logger.info(jsonrepl)
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

    #logger.info("\n\n jsonfooter : \n" + jsonfooter)
    fulljson = jsonheader+jsonstr+jsonfooter

    #logger.info("\n\n fulljson : \n" + fulljson)
    print(fulljson)

    dictjson = json.loads(fulljson)

    #print(dictjson)
    #places = place.objects.filter(category_group_code='01')
    return JsonResponse(dictjson)
