import requests
import match_type 
import division




# api키
with open('fifaapi.txt','r') as f:
    api_key=f.read()

user_info_url="https://api.nexon.co.kr/fifaonline4/v1.0/users"
headers = {'Authorization' : api_key}

# 검색할 아이디 입력
nickname=input("검색할 아이디를 입력해주세요: ")
params={'nickname':f'{nickname}'}




# 고유식별자 아이디
resp=requests.get(user_info_url,params=params,headers=headers)
access_id=resp.json().get('accessId')
print(access_id)

# 디비전
division_dict=division.get_division_type_dict(headers)
# 매치 정보
match_dict = match_type.get_match_type_dict()


# 유저 최고등급 조회
umi_url=f"https://api.nexon.co.kr/fifaonline4/v1.0/users/{access_id}/maxdivision"
response=requests.get(umi_url,headers=headers)
match_types=response.json()

official_match_type = match_types[0]['matchType']  
official_match_achievement_date = match_types[0]['achievementDate'][:-9]
official_match_division=match_types[0]['division']

# coach_match_type = match_types[1]['matchType']
# coach_match_achievement_date = match_types[1]['achievementDate'][:-9]

print(f'{nickname}님의 최고티어 정보입니다.')
print("모드: ",match_dict.get(official_match_type))
print("최고 티어: ",division_dict.get(official_match_division))
print("기간: ",official_match_achievement_date)




