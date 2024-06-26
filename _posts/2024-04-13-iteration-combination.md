---
title: "TIL: itertools 없이 순열과 조합"
date: 2024-04-12T15:47:49.642Z
tags:
  - TIL
  - Python
categories:
  - PS
lastmod: 2024-04-12T17:19:57.958Z
sitemap:
  changefreq: daily
  priority: 1
---

삼성 코테에서는 sys 도 못쓰고 itertools도 못쓴다니.
deque 쓰게해줘서 고마울지경.

순열과 조합 모두 DFS, 백트래킹과 유사하게 진행된다고 한다.<br>
으아 헷갈리~

- BT는 이제 promising 하면 재귀, 아니면 pruning.
- BFS는 이제 not visited한 곳이고 promising 하면 큐에 추가.
- DP는 이제 dp에 없는데면 두가지의 경우를 나누어서 재귀하고 그 중 나은 애로 저장.

## Combination 조합

- combination([0,1,2,3], 2) = ([0],combination([1,2,3], 1)) + ([1],combination([2,3], 1)) + ([2],combination([3], 1)))

### Code

- DP처럼 이걸 선택한 경우 안한경우 이렇게 할라 했더니, ~~이건 순열임ㅋㅋ~~ 아놔 그냥 바보인거임. 순열도 이거보다 간단하게 해결 ㄱㄴ.
  DP처럼 하려면 그냥 둘 중 하나 선택을 해야함. 지금은 계속 반복저장이라 쓰면안된다.<br>
  그래서 아예 [[]] 형식으로 리턴하는 것
- 조합은 앞에 선택한 경우 하나보고, 그 뒤로는 그냥 없이 함.

```py
def combination(arr, n):

    ans = []

    if n<=0:
        return [[]]

    for i in range(len(arr)):
        choose = arr[i]
        rest = arr[i+1:]
        for C in combination(rest, n-1):
            ans.append([choose]+C)
            # 충격. [] + [] = []리스트 하나로 합쳐줌.ㄹㅇ;;
    return ans
```

## Permutation 순열

- permutation([0,1,2,3], 2) = ([0],permutation([1,2,3], 1)) + ([1],permutation([0,2,3], 1)) + ([2],permutation([0,1,3], 1))+ ([3],permutation([0,1,2], 1))

### Code

```py
def permutation(arr, n):

    ans = []

    if n<=0:
        return [[]]

    for i in range(len(arr)):
        choose = arr[i]
        rest = arr[:i]+arr[i+1:]
        for C in permutation(rest, n-1):
            ans += [[choose]+C]
            #이 경우에는 append가 아니라 ans에 더해가는 식이라, 안에 있는 리스트 타입의 순열들이 하나의 큰 리스트에 들어가게됨.

    return ans
```
