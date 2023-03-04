import requests

def get_spid_dict():
    spid_url="https://static.api.nexon.co.kr/fifaonline4/latest/spid.json"
    spid_info=requests.get(spid_url)

    spid_id=[data['id'] for data in spid_info.json()]
    spid_name=[data['name'] for data in spid_info.json()]

    spid_dict={}
    for i in range(len(spid_id)):
        spid_dict[spid_id[i]]=spid_name[i]
        
    return spid_dict
