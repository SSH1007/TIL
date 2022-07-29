import requests
from pprint import pprint
import xmltodict
import json

def credits(year,month):
    pass 
    # 여기에 코드를 작성합니다.
    api_key = 'EgN5dzA1OcTdb2FWtrqXSke%2BhhrSIp8GxuNWPjQu4suOPSVpG2eudLjujo7UR6sblLD0cXybqxVjRSGgUHP2ow%3D%3D'
    search_URL = f'http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/getHoliDeInfo?solYear={year}&solMonth={month}&ServiceKey={api_key}'  
    
    response = requests.get(search_URL) # 해당 API는 XML을 반환함

    xmldic = xmltodict.parse(response.text) # xml(response.txt)을 dictionary로 파싱한다. 

    
    print(year,month)

    if xmldic['response']['body']['items'] == None:
        print('휴일이 없습니다.')
        return None
    
    lst = []
    dict3 = xmldic['response']['body']['items']['item']

    if type(dict3) is dict:
        if dict3['isHoliday']=='Y':
            lst.append((dict3['dateName'],dict3['locdate']))
    elif type(dict3) is list:
        for i in dict3:
            if i['isHoliday']=='Y':
                lst.append((i['dateName'],i['locdate']))

    if len(lst)==0:
        print('휴일이 없습니다.')
        return None
    else:
        for l in lst:
            print (l)



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    2022년 휴일 출력
    """
    for i in range(1,13):
        if i < 10:
            credits('2022','0'+str(i))
        else:
            credits('2022',i)