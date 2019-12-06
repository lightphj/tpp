import pandas as pd
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def get_url(item_name, code_df): 
    code = code_df.query("name=='{}'".format(item_name))['code'].to_string(index=False) 
    url = 'http://finance.naver.com/item/sise_day.nhn?code={code}'.format(code=code) 
    print("요청 URL = {}".format(url)) 
    return url 
    
'''
def StockData(request):
    code_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13', header=0)[0] 
    
    # 종목코드가 6자리이기 때문에 6자리를 맞춰주기 위해 설정해줌 
    code_df.종목코드 = code_df.종목코드.map('{:06d}'.format) 
    # 우리가 필요한 것은 회사명과 종목코드이기 때문에 필요없는 column들은 제외해준다. 
    code_df = code_df[['회사명', '종목코드']] 
    # 한글로된 컬럼명을 영어로 바꿔준다. 
    code_df = code_df.rename(columns={'회사명': 'name', '종목코드': 'code'})
    code_df.head()

    # 신라젠의 일자데이터 url 가져오기 
    item_name='현대오토에버'
    url = get_url(item_name, code_df) 
    
    print(url)
    # 일자 데이터를 담을 df라는 DataFrame 정의 
    url='https://finance.naver.com/item/sise_day.nhn?code=307950'

    df = pd.DataFrame() 
    # 1페이지에서 20페이지의 데이터만 가져오기 
    for page in range(1, 2): 
        pg_url = '{url}&page={page}'.format(url=url, page=page) 
        df = df.append(pd.read_html(pg_url, header=0)[0], ignore_index=True) 

    # df.dropna()를 이용해 결측값 있는 행 제거 
    df = df.dropna() 
    msg = df['종가'][1].astype(int)
    #msg = df
    # 상위 5개 데이터 확인하기
    return render(request, 'index.html', {'message': msg})
'''

@csrf_exempt
def StockSkill(request):
    code_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13', header=0)[0] 
    
    # 종목코드가 6자리이기 때문에 6자리를 맞춰주기 위해 설정해줌 
    code_df.종목코드 = code_df.종목코드.map('{:06d}'.format) 
    # 우리가 필요한 것은 회사명과 종목코드이기 때문에 필요없는 column들은 제외해준다. 
    code_df = code_df[['회사명', '종목코드']] 
    # 한글로된 컬럼명을 영어로 바꿔준다. 
    code_df = code_df.rename(columns={'회사명': 'name', '종목코드': 'code'})
    code_df.head()

    # 신라젠의 일자데이터 url 가져오기 
    item_name='현대오토에버'
    url = get_url(item_name, code_df) 
    
    print(url)
    # 일자 데이터를 담을 df라는 DataFrame 정의 
    url='https://finance.naver.com/item/sise_day.nhn?code=307950'

    df = pd.DataFrame() 
    # 1페이지에서 20페이지의 데이터만 가져오기 
    for page in range(1, 2): 
        pg_url = '{url}&page={page}'.format(url=url, page=page) 
        df = df.append(pd.read_html(pg_url, header=0)[0], ignore_index=True) 

    # df.dropna()를 이용해 결측값 있는 행 제거 
    df = df.dropna() 
    msg = df['종가'][1].astype(int)
    

    jsonstr = '''
    {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "basicCard": {
                        "title": " 현대오토에버 주가",
                        "description": "'''+ str(msg) + '''",
                        "buttons": [
                            {
                                "action": "webLink",
                                "label": "상세보기",
                                "webLinkUrl": "http://stock.kakao.com/m/stocks/KOREA-A307950"
                            },
                            {
                                "action": "message",
                                "messageText": "처음으로",
                                "label": "처음으로"
                            }
                        ]
                    }
                }
            ]
        }
    }
    '''
    #logger.info("\n\n fulljson : \n" + fulljson)
    print(jsonstr)

    dictjson = json.loads(jsonstr)

    #print(dictjson)
    #places = place.objects.filter(category_group_code='01')
    return JsonResponse(dictjson)