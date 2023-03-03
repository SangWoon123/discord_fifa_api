import requests

def get_division_type_dict(headers):
    # 디비전
    division_url="https://static.api.nexon.co.kr/fifaonline4/latest/division.json"
    response=requests.get(division_url,headers=headers)
    division_ids=[data['divisionId'] for data in response.json()]
    division_names = [data["divisionName"] for data in response.json()]

    # 딕셔너리 형태 변환
    divisions = {}
    for i in range(len(division_ids)):
        divisions[division_ids[i]]=division_names[i]
    return divisions