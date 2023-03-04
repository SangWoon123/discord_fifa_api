import requests
import match_type 
import division
from module import get_accessid
from module import spid

# api키
with open('fifaapi.txt','r') as f:
    api_key=f.read()

headers = {'Authorization' : api_key}


# url 변수
#nickname=input("닉네임을 입력해주세요: ")
access_id=get_accessid.get_user_access_id(nickname='아스날우승은가능')

tradetype='buy'
offset=0
limit=30


trade_url=f"https://api.nexon.co.kr/fifaonline4/v1.0/users/{access_id}/markets?tradetype={tradetype}&offset={offset}&limit={limit}"

trade_info=requests.get(trade_url,headers=headers).json()

trade_date_list=[data['tradeDate'][:-9] for data in trade_info]
trade_grade_list=[f"{data['grade']}강" for data in trade_info]
trade_value_list=[data['value'] for data in trade_info]
trade_spid_list=[data['spid'] for data in trade_info]

#trade_grade_list=list(map(lambda num: str(num) + '강', trade_grade_list))


# 모듈에서 가져온 데이터
spid_info_dict=spid.get_spid_dict()



# print("거래 유형: ",tradetype)

for i in range(limit):
    pid=trade_spid_list[i]
    print("거래날짜: ",trade_date_list[i])
    print("선수: ",spid_info_dict.get(trade_spid_list[i]))
    print("강화: ",trade_grade_list[i])
    print("가격: ",trade_value_list[i])



