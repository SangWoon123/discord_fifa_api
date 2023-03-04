import requests


# API 키
with open('fifaapi.txt', 'r') as f:
    api_key = f.read()

USER_INFO_URL = "https://api.nexon.co.kr/fifaonline4/v1.0/users"
HEADERS = {'Authorization': api_key}


def get_user_access_id(nickname):
    """
    닉네임으로 고유식별자 아이디 조회
    """
    params = {'nickname': nickname}
    response = requests.get(USER_INFO_URL, params=params, headers=HEADERS)
    response.raise_for_status()
    return response.json().get('accessId')

