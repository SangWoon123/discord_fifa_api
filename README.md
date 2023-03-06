# discord_fifa_api

</br> 2023-03-03 </br>챗봇 명령어: !최고티어 (nickname)
</br> 2023-03-04 </br>챗봇 명령어: !거래 (nickname) (buy or sell)

## 소개
디스코드 챗봇 + fifa4 online 공식 api 활용: 유저 정보 검색기
<img width="1043" alt="스크린샷 2023-03-04 오후 1 16 45" src="https://user-images.githubusercontent.com/100204926/222875255-a5a431cf-8d97-4f43-bfd8-2d323a88fe99.png">피파온라인 공식 api 유저정보 부분을 활용 

## 기능정보
유저의 최고티어</br>
유저의 거래내역 최근 10개



## 모듈정보

division 모듈 반환정보</br>
-타입: dict</br>
-정보: 경기모드</br>

match_type 모듈 반환정보</br>
-타입: dict</br>
-정보: 티어정보</br>

get_accessid 모듈 반환정보</br>
-타입: str</br>
-정보: 유저고유id</br>

spid 모듈 반환정보</br>
-타입: dict</br>
-정보: 선수 고유 id 와 선수 이름</br>

## 사용법
피파 개발자센터에서 발급받은 키를 "fifaapi.txt" 파일과
      </br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;디스코드 개발자센터에사 발급받은 키를 "token.txt" 파일에 저장후 
      </br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"main.py" 실행
      </br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;디스코드내에 챗봇 초대 필수

## 실행결과
</br><img width="191" alt="스크린샷 2023-03-04 오전 2 05 18" src="https://user-images.githubusercontent.com/100204926/222782689-525cb383-9c4a-427c-8af3-8da881a85938.png">
</br> 다음과 같은 실행결과가 나오면 embed.py가 정상적으로 실행되었다는 의미
</br>
</br>
</br><img width="300" alt="스크린샷 2023-03-04 오후 1 11 42" src="https://user-images.githubusercontent.com/100204926/222875128-a1f42226-e872-443f-a105-7ac47bc3451e.png"> <img width="497" alt="222787259-37a6abc7-5102-4ab6-85da-be1ab59771ed" src="https://user-images.githubusercontent.com/100204926/223003642-3552ce52-ff58-451e-a985-ced1b3745ddd.png">
</br> 디스코드 창에서 접두사 !을 넣어 "!최고티어" + 피파유저네임 입력하면 정상적으로 동작한다


### 부족한점
거래내용에서 썸네일로 선수이미지 제공 기능을 구현하고싶었으나 실력부족으로 코드가 복잡해져서 포기

### 시도해볼만한점
추후 Sping으로 구현해볼 것 + 유저정보탭 api 뿐만아니라 모든 api 사용하여 웹페이지 제작
