import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))) #상위 폴더 임포트
from discord.ext import commands
import discord
import requests
import match_type 
import division
from module import get_accessid
from module import spid

class Trade(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Trade Cog is Ready")
        
    @commands.command(name = "거래")
    async def trade(self,ctx,args1,args2):
        nickname=args1
        tradetype=args2
        offset=0
        limit=10
        # api키
        with open('fifaapi.txt','r') as f:
            api_key=f.read()

        headers = {'Authorization' : api_key}
        access_id=get_accessid.get_user_access_id(nickname)
        trade_url=f"https://api.nexon.co.kr/fifaonline4/v1.0/users/{access_id}/markets?tradetype={tradetype}&offset={offset}&limit={limit}"

        # 요청
        trade_info=requests.get(trade_url,headers=headers).json()

        # 파싱
        trade_date_list=[data['tradeDate'][:-9] for data in trade_info]
        trade_grade_list=[f"{data['grade']}강" for data in trade_info]
        trade_value_list=[data['value'] for data in trade_info]
        trade_spid_list=[data['spid'] for data in trade_info]
        # 모듈에서 가져온 데이터
        spid_info_dict=spid.get_spid_dict()

        embed=discord.Embed(
            title="최근 10개 거래정보",
            color=discord.Color.green()
        )
        
        for i in range(len(trade_info)):
            embed.add_field(name=i+1,value="")
            embed.add_field(name="선수",value=spid_info_dict.get(trade_spid_list[i]))
            embed.add_field(name="강화",value=trade_grade_list[i])            

        embed.set_footer(text=f"마지막 거래날짜는 {trade_date_list[0]} 입니다.")
        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(Trade(client))