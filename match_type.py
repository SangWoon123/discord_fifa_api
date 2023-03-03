import requests

# 매치종류
def get_match_type_dict():
    response=requests.get("https://static.api.nexon.co.kr/fifaonline4/latest/matchtype.json")
    match=response.json()

    match_type=[data['matchtype'] for data in match]
    desc=[data['desc'] for data in match]


    match_dict={}
    for i in range(len(match_type)):
        match_dict[match_type[i]]=desc[i]
    return match_dict