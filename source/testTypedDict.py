from typing import TypedDict

# 내가 지정한 타입만 들어가는 나만의 dict 생성
class Person(TypedDict):
    name : str
    age : int
    job : str

typed_dict1 : Person = {'name' : '홍길동', 'age':24, 'job':'의적'}

# age를 문자열로 변경
typed_dict1['age'] = '35'

# 새로운 key 추가
typed_dict1['region'] = '장성'
