---
title: "TIL: Programmers: 나누어 떨어지는 수"
date: 2024-04-05T16:19:53.574Z
tags:
  - TIL
  - Programmers
  - Lv1
categories:
  - PS
description: 단순 조건문은 한줄에 정리하기
lastmod: 2024-04-05T16:19:53.574Z
sitemap:
  changefreq: daily
  priority: 1
---

<a href = 'https://school.programmers.co.kr/learn/courses/30/lessons/12910'>나누어 떨어지는 수</a>

비기너 문제여서 간단히 성공할 수 있었다.

하지만 내 코드는 너무 길었다...

### 내 코드

```py
def solution(arr, divisor):
    answer = []

    for i in arr:
        if i%divisor==0:
            answer.append(i)
    if answer==[]:
        answer.append(-1)
    return sorted(answer)
```

난 너무 코드를 구현만 한다. 문제에서 말하는 순서 그대로..

### 예시코드

```py
def solution(arr, divisor):
  return sorted([n for n in arr if n%divisor == 0]) or [-1]
```

내가 제일 못하는거:

1. [n &nbsp;for n in arr &nbsp; &nbsp;if n%d==0]

   나는 이 for in if 구조가 계속 머리에 안들어온다.
   단순한 if문이면 기억하자.

2. else [-1]

   아니 난 멍청이다.
   "앞에 아무것도 없을 때 : [-1]을 하기."
   맨날 이런식이었는데,
   그냥 else [-1] 리턴 이러면 되는거였어..
