---
title: "TIL: 코테 공부도 방법이 있구나"
date: 2024-04-07T17:06:33.708Z
tags:
  - TIL
  - 맵 탐색
  - 그래프 탐색
  - 값 찾기
categories:
  - Algorithm
lastmod: 2024-04-10T05:53:59.380Z
sitemap:
  changefreq: daily
  priority: 1
---

오늘이 되어서야 여러 친구들한테 코테 공부법을 물어봤다.
<br>역시 이것도 막무가내로 공부하는게 아니었어,,난 바부팅이.

내 계획은

- **받은 알고리즘 마인드맵 저 내용 완벽 숙지**
- **백준 삼성역테 기출 45문제를 월-토 6일동안 풀기. 하루에 최소 5문제는 풀어야 그나마 눈에 익을 듯.**

매드캠프 바이브 on.
<br>정말 나에게 소중한 시간이었구나 매드캠프가..

---

# 알고리즘 문제 종류

일단 받은 거 베끼면서 읽어보자

## 1. 맵 탐색

1.  여러 경우의 수를 모두 시뮬레이션 -> **BT**
2.  시작점이 있고 뻗어나가는 경우 -> **BFS**
3.  요소들이 각 비트로 표현이 됨(on/off) -> **BitMasking**

---

-> 난 지금까지 알고리즘을 외우고 그게 어떤 문제에 적용되나를 생각했는데<br>
그게아니라 문제유형을 나누고 알고리즘을 적용하는거였구나.

- BT는 들어도 들어도 적응이 안됨.

  막히면 그 전단계로 돌아가는 재귀함수식 유형.
  다음으로 넘어갈만 한지 체크하고 재귀를 하고 부모노드로 돌아가는 형태. 체킹하는
  함수도 따로 만들면 좋음.

- BFS는 heapq 쓰는거.
- bitmasking은 처음 들어봤다.

---

## 2. 그래프 탐색

1. 모든 노드를 최소비용으로 연결함. => 최소 신장 트리.
   1. 노드가 많고 간선이 적은 경우 -> **크루스칼**
   2. 간선이 많은 경우. -> **프림**
2. 하나의 노드에서 다른 모든 노드로 가는 최소비용 -> **다익스트라**
3. 모든 노드에서 다른 모든 노드로 가는 최소비용 -> **플로이드**
4. 특정 노드에 도달하기 위해서는 거쳐야할 노드들이 정해져 있을 때 줄 세우기.-> **위상 정렬.**

-> 그래프 알고리즘은 이름이 비슷하게 생겼어 진짜. 노드와 간선 중요.

---

- 모든 노드를 최소로 연결. != 모든 노드에서 다른 모든 노드로 가는 비용.

  전자는 약간 도시 사이에 다리 놓는 문제 느낌. 후자는 노드와 노드 사이에 다른게 끼어있는 느낌?

- 하나의 노드에서 모든 노드는 다익스트라. 꼭 외워야함.
- 각각의 알고리즘 코드를 외워야함.

---

## 3. 값 찾기

### 1. 최선의 값 찾기

1. 매번 최선의 선택이 결과적으로도 최선. -> **Greedy.**
2. 수학적인 공식은 몰라도, 단계적으로 하면 결과적으로 최선. -> **DP**

   1. 시작값을 알고있고, 시작부터 결과까지 단계별로 값을 쌓음.

      **바텀엄 DP**

   2. 최종 값을 알고있고, 결과부터 시작까지 값을 쌓음.

      **Top-Down DP**

### 2. 특정 값 찾기

1. 정렬이 가능한가?
   1. 하나의 값을 찾을 때 -> **이진탐색**
   2. 두 값의 계산을 통해 찾을 때 -> **Two Pointer**
2. N개 중 M개를 선택. 조합 -> **BT**
3. 수열에서 가장 긴 증가하는 부분수열의 길이를 구한다 -> **LIS**
4. 수열에서 증가하는 혹은 감소하는 부분수열을 찾는다 -> **스택**
5. 특정 구간의 값으 구한다 -> **세그멘테이션 트리**
6. 영단어를 앞글자붜 파례로 탐색하며 단어를 찾는다 -> **트리**

---

그리디는 수학적이어야 하는구나.

주로 난 DP를 하는데, 시간이 긴데 싶으면 그리디인것.

- 바텀업. DP테이블(2차원배열) 활용. 맨 처음 값 dp에 저장하고 for문.
- 탑다운. 메모제이션 활용. 재귀함수 호출. 탈출문이 맨 위에.
  스택크기 한정

---

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FMRqyW%2FbtsFaDLqLDG%2FEWRBxFX2lXCg7slVbazblK%2Fimg.png)

[출처 티스토리](https://vina98.tistory.com/m/8)