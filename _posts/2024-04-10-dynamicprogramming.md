---
title: "TIL: DP"
date: 2024-04-10T05:12:08.240Z
tags:
  - TIL
  - 값 찾기
  - 알고리즘
  - DP
categories:
  - PS
lastmod: 2024-04-10T05:12:14.421Z
sitemap:
  changefreq: daily
  priority: 1
slug: til-dp
---

# 다이나믹 프로그래밍. 동적 프로그래밍.

- 이전 값을 저장하고(캐싱) 사용
  무엇을 어떻게 저장할 지 중요함
- 점화식 중요

---

**이 내용 전부 무시. 아래에 다시 개념정리함**

- 바텀업(전형적인 다이나믹 프로그래밍) → <U>DP테이블(2차원)</U> 활용

시작값을 알고있고, 시작부터 결과까지 단계별로 값을 쌓음.<br>
**반복문**<br>
맨 처음에 대한 값 dp에 저장하고 for문으로 남은 인덱스 처리

- 탑다운

최종 값을 알고있고, 결과부터 시작까지 값을 쌓음.<br>
**재귀함수**<br>
큰 문제를 해결하기 위해 작은문제를 호출<br>
<U>재귀함수를 호출</U>하고, <U>탈출문이 맨 위에</U> 있는 형식.<br>
-> 시스템상 재귀함수의 스택 크기가 한정될 수 있음

---

바텀업이랑 탑다운이랑 다 그냥 헷갈리는 쓰잘데기 없는 거였음.<br>
**DP는 탑다운**으로 풀면 된다고 생각하면 된다.

문제를 보는데, **선택의 가짓수가 있고 그걸로 조합을 만들어야하는** 경우면<br>
DP를 쓰면 됨.<br>
그리디로 하기엔 매 순간의 선택이 최적이 아니니까.

근데 재귀를 하면, 값이 커질수록 무조건 시간초과가 뜸.<br>
피보나치 수열을 생각하면 편함.<br>
재귀 두번 하자마자, 똑같은 값으로하는 똑같은 계산을 반복 진행해야하는 경우가 생김.

그래서 **캐싱 할 dp**를 만드는거임.<br>
약간 BFS에서 visited하는 것과 유사.<br>
BFS, DFS, DP, 브루트포스(완전탐색), 다 유사하게 생긴 아이.

### Code

- 함수의 형태는 아래 코드처럼 크게 세가지. 탈출조건, 선택, 리턴.

```py
import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline

#N일 <=15
#T일소요 <=5
#P 금액<=1000

N = int(input())
#리스트로 받을거라면 이런 멋진 방법이 있다.
# schedule = [list(map(int, input().split(' '))) for _ in range(N)]

#근데 너무 헷갈려서 T랑 P랑 나누겠음.
#이거 1일부터 이런거면 무조건 N+1로 가자. 대신 함수호출할 때 시작값이 1이어야함!!
T = [0]*(N+1)
P = [0]*(N+1)

for i in range(1,N+1):
    t,p = map(int, input().split(' '))
    T[i] = t
    P[i] = p

dp=[0]*(N+1)

def topdown(index):
    #종료
    #인덱스 기준, 이 함수 재귀의 끝
    if index>N:
        return 0

    #조건 기준, 이 날짜에 상담 불가한 경우
    if index+T[index]>N+1:
        return topdown(index+1)

    #캐싱. 값이 존재하면 아래 계산 안함.
    if dp[index]>0:
        return dp[index]

    #선택
    doSangdam = topdown(index+T[index])+P[index]

    noSangdam= topdown(index+1)

    dp[index] = max(doSangdam, noSangdam)

    #리턴
    return dp[index]

print(topdown(1))
```

### 대표유형

[백준 퇴사](https://www.acmicpc.net/problem/14501)

- 중요한건 테케 돌리기. 틀리기위해 돌리는거다라는 마음가짐으로 계속 돌려봐야함.
- 이날 상담을 하냐, 안하냐 이걸 나누는게 일단 DP의 시작.
  그 다음 중요한건 상담을 하는 경우의 값, 상담을 안하는 경우의 값.
  - 상담을 하는 경우: 이 상담이 끝나는 날부터의 제일 좋은 비용과 이 상담비용을 더함.
  - 상담을 안하는 경우: 바로 다음날의 제일 좋은비용으로 넘어감.

[백준 평범한 배낭](https://kau-algorithm.tistory.com/1135)

- 이 역시, 물건을 선택할지말지. 이게 DP의 시작.
  - 선택하는 경우: 이 물건을 선택해서 추가된 무게에서 다음물건 선택할지말지로 넘어가고, 거기에 이 물건의 가치를 더함.
  - 안선택하는 경우, 그냥 다음물건 선택할지말지로 바로 넘어가면 됨.

[백준 Dance Dance Revolution](https://www.acmicpc.net/problem/2342)
