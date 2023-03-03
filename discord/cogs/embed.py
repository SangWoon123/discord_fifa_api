import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))) #상위 폴더 임포트
from discord.ext import commands
import discord
import requests
import match_type 
import division


class Embed(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("embed Cog is Ready")
        
    @commands.command(name = "최고티어")
    async def embed(self, ctx,args):
        nickname=args
        # api키
        with open('fifaapi.txt','r') as f:
            api_key=f.read()
        headers = {'Authorization' : api_key}
        params={'nickname':f'{nickname}'}


        user_info_url="https://api.nexon.co.kr/fifaonline4/v1.0/users"


        # 유저 고유식별 아이디
        resp=requests.get(user_info_url,params=params,headers=headers)
        access_id=resp.json().get('accessId')

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


        # 본문
        embed=discord.Embed(
            title="당신의 최고티어는?",
            color=discord.Color.green()
        )
        embed.add_field(name="유저닉네임: ",value=nickname,inline=False)
        embed.add_field(name="모드: ",value=match_dict.get(official_match_type),inline=True)
        embed.add_field(name="최고티어: ",value=division_dict.get(official_match_division),inline=True)
        embed.add_field(name="달성날짜: ",value=official_match_achievement_date,inline=True)

         # 링크 포함 헤더
        embed.set_author(
        name="못참겠다 피파하러가즈아!", 
        url="https://fifaonline4.nexon.com/main/index", 
        icon_url="https://oopy.lazyrockets.com/api/v2/notion/image?src=https%3A%2F%2Fth.bing.com%2Fth%2Fid%2FOIP.PfSFXftUSnUWIdhFPImbhwAAAA%3Fpid%3DImgDet%26rs%3D1&blockId=f6f97693-8a2b-47b9-8188-e8099c6d2965&width=256")

        
        # 이미지
        embed.set_image(url="https://upload2.inven.co.kr/upload/2019/12/19/bbs/i16179180516.png")

        # 푸터
        embed.set_footer(text="피파공식 api를 이용한 검색결과 입니다.")

        await ctx.send(embed=embed)
        

async def setup(client):
    await client.add_cog(Embed(client))