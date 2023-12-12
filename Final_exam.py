#<오픈소스프로그래밍 기말 프로젝트>
#
# ● 아래의 코드를 수정 혹은 프로그래밍하여 문제를 해결하시오.
# ● 문제의 점수는 각각 표시되며, 부분점수가 존재합니다.
#
# 학번 : 20171751 이름 : 이정현

import os
import time

# Q.1 10점
#
# 문자열 my_string과 target이 매개변수로 주어질 때,
# target이 문자열 my_string의 부분 문자열이라면 1을,
# 아니라면 0을 return 하는 solution 함수를 작성하시오.
#
# 제한사항
# 1 ≤ my_string 의 길이 ≤ 100
# my_string 은 영소문자로만 이루어져 있습니다.
# 1 ≤ target 의 길이 ≤ 100
# target 은 영소문자로만 이루어져 있습니다.

def solution(my_string, target):
    s1 = my_string.lower()   #my_string을 소문자로 변경
    s2 = target.lower()          #target을 소문자로 변경
    if (len(s1) >= 1 and len(s1) <= 100) and (len(s2) >= 1 and len(s2) <= 100):
    #my_string과 target의 길이가 전부 1이상 100이하 일때 실행
        if s2 in s1:  #my_string이라는 문자열 안에 target이 있는가를 설정하는 조건문
            answer = 1                  #위의 조건문에 만족하면 True이기에 answer은 1을 가진다
        else:                                 #my_string이라는 문자열 안에 target이 없는 경우에 answer은 0을 가진다
            answer = 0
    else: #my_string과 target의 길이 중 하나라도 1미만 100초과일때 answer에 error를 반환
        answer = 'error'
    return answer

# Q.2 10점
#
# 모스부호 해독 프로그램 만들기
# 문자열 letter 가 매개변수로 주어질 때,
# letter 영어 소문자로 바꾼 문자열을 return 하는
# solution 함수를 완성하시오.
#
# 제한사항
# 1 ≤ letter 의 길이 ≤ 1,000
# letter 의 모스부호는 공백으로 나누어져 있습니다.
# letter 에 공백은 연속으로 두 개 이상 존재하지 않습니다.
#
# letter = 여러분의 좌우명 또는 인상 깊었던 말을 쓰시오.

def solution(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}
    answer = ''
    s1 = letter.split(' ') # letter의 공백을 기준으로 나누어 list 자료형으로 바꾼다.
    if len(s1) >= 1 and len(s1) <= 1000:  #letter의 list 자료형의 수가 1이상 1000이하 일때 실행
        for i in s1:       # letter를 공백을 기준으로 나눈 s1이라는 리스트를 i에 하나씩 할당하면서 반복하고있다
            if i in morse:   # s1에서 할당받은 요소인 i가 morse 딕셔너리에 존재한다면 실행한다
                answer += morse[i]   #morse의 i라는 key가 가진 value를 answer에 추가한다.
            else:          #모스부호가 아닌 다른 글자나 기호가 들어왔다면 error를 answer에 반환
                answer = 'error'
    else: #letter의 list 자료형의 수가 1미만 1000초과라면 error를 answer에 반환
        answer = 'error'
    return answer
#for에서 in과 if에서 in은 다른 요소이다.

# Q.3 10점
#
# 행성의 나이를 알파벳으로 표현할 때,
# a는 0, b는 1, ..., j는 9
# 예를 들어 cd는 23살, fb는 51살입니다.
# age가 매개변수로 주어질 때
# PROGEAMMER-857식 나이를 return 하도록
# solution 함수를 완성하시오.
#
# 제한사항
# age는 자연수입니다.
# age ≤ 1,000
# PROGRAMMERS-857 행성은 알파벳 소문자만 사용합니다.

def solution(age):
    answer = 'PROGRAMMERS-'
    age_list={'0':'a','1':'b','2':'c','3':'d','4':'e','5':'f','6':'g','7':'h','8':'i','9':'j'}
    #나이와 알파벳을 묶은 딕셔너리 제작
    if (age > 0 and age <= 1000) and age - int(age) == 0: #age가 1000이하 자연수 인지 확인하는 조건
        new_age = str(age)#age 문자열로 변환하여 new_age에 넣음
        for i in new_age:#new_age의 요소를 i에 넣음  
            answer += age_list[i]#answer에 숫자에 맞는 문자를 age_list에서 찾아 대입
    else:
        answer = 'error'
    return answer

# Q.4 10점
#
# x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인
# 서로 다른 크기의 원이 두 개 주어집니다.
# 반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때,
# 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를
# return하도록 solution 함수를 완성해주세요.
# ※ 각 원 위의 점도 포함하여 셉니다.
#
# 제한사항
# 1 ≤ r1 < r2 ≤ 1,000,000

def solution(r1, r2):
    answer = 0
    return answer

# Q.5 10점
#
# 0 또는 양의 정수가 주어졌을 때,
# 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.
#
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어
# return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
#
# numbers = [8, 30, 17, 2, 23]

def solution(numbers):   
    if (len(numbers) >= 1 and len(numbers) <= 100000) and (max(numbers)<=1000 and min(numbers)>=0):
        #numbers의 길이가 1이상 100000이하 이고 원소의 크기를 max와 min을 이용해 0이상 1000이하로 조건 설정
        s1 = list(map(str, numbers))# 주어진 숫자 배열을 문자열로 변환 후 list로 만듦
        s1.sort(key=lambda x: x * 3, reverse=True) #문자열을 lambda x를 key로 분류하고 내림차순으로 정렬한다
        answer = ''.join(s1) # 정렬된 s1을 문자열로 공백없이 answer에 결합
    else: #조건에 만족하지 않다면 answer에 error 반환
        answer = 'error'
    return answer
