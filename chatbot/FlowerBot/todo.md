# Intent

꽃 종류/목적, 가격대, 포장(바구니/다발/상자), 배송(퀵/택배/직접수령), 

추가 정보 (받는 사람, 보내는 사람, 남길 말, 주소, 날짜, 결제)

API  def flowerOrder(꽃 종류, 추가정보, 포장, 가격대, 배송=택배): # provide

text def expConfirm(slots)

text def impConfirm(slots)

text def Apology(slots)

text def Request(slots)

text def greeting(hi/bye)

text def retrieve()

text def askFor()


# ENTITY Extract

PER
ORG
LOC
MISC (목적 : //결제/입금...)
PRD 꽃바구니/꽃다발/꽃상자/축하화환/근조화환
EVE(목적) 축하/기념일/개업/이전/승진/취임/결혼/행사/추모/근조/애인
INT(발화 의도)
BILL 카드/계좌/결제 등..
O

## feature

Ÿ 어휘 자질: (-2,-1,0,1,2) 위치에 해당하는 형태소 어휘 정보. 
Ÿ 접미사(suffix) 자질: (-2,-1,0,1,2) 위치에 해당하는 형태소 어휘의 접미사(suffix)
정보. 
Ÿ 형태소 태그 자질: (-2,-1,0,1,2)위치에 해당하는 형태소의 POS tag 정보. 
Ÿ 형태소 태그 + 길이 자질: 형태소의 태그 정보와 형태소의 길이 정보 조합
Ÿ 형태소의 어절 내 위치: 형태소가 어절의 시작, 중간, 끝 위치에 있는 지에 대
한 정보
Ÿ 개체명 사전 + 길이 자질: 개체명 사전에 존재하는 지에 대한 정보와 형태소
의 길이 정보 조합
Ÿ 개체명 사전 자질 + 형태소 길이 정보
Ÿ 15개의 정규 표현식: [A-Z]*, [0-9]*, [0-9][0-9], [0-9][0-9][0-9][0-9], [A-Za-z0-9]*,
… .

## Parser

날짜 parser
시간 parser
주소 parser
가격 parser
