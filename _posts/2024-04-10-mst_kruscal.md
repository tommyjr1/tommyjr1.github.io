---
title: "TIL: MST 크루스칼 알고리즘"
date: 2024-04-09T23:18:59.720Z
tags:
  - TIL
  - 그래프 탐색
  - MST
categories:
  - Algorithm
lastmod: 2024-04-10T00:16:29.906Z
sitemap:
  changefreq: daily
  priority: 1
---

이번에는 그래프다!<br>
MST: 최소 신장 트리. 즉 사이클이 없는 트리에서 모든 간선이 최소비용.
**모든 노드를 이어야 할 때**

그 중 노드가 많고 간선이 적을 때면 크루스칼.

## Code

- 간선 정보와 부모노드 정보 두개의 리스트 필요.
- 간선비용 작은 순서대로 진행.
  -> heapq를 쓰면? 어우 안 알아보면 큰일날뻔. 아래에 씀

- 간선 양옆의 노드의 부모 노드가 다르면 MST에 넣고 부모 값이 큰 애의 부모를 작은애로 바꿈.

```py
import sys

sys.stdin = open('../input.txt', 'r');

def find_parents(parents, i):
    if parents[i]!=i:
        parents[i] = find_parents(parents, parents[i])
    return parents[i]
def union(parents, a,b):
    pa = find_parents(parents, a)
    pb = find_parents(parents, b)
    if pa<pb:
        parents[pb] = pa
    else:
        parents[pa] = pb

if __name__ =='__main__':
    N = int(input())
    M = int(input())

    parents = [0] * (N + 1)
    for i in range(N + 1):
        parents[i] = i

    edges = []
    for i in range(M):
        a, b, c = map(int, input().split(' '))
        edges.append((a, b, c))
        #heapq.heappush(edges, (c,a,b))


    edges = sorted(edges, key=lambda x: x[2]);
    cost=0
    for i in edges:
        a,b,c = i
        if find_parents(parents, a)!=find_parents(parents, b):
            print(a,b)
            union(parents, a,b)
            cost+=c;
    print(cost)
```

## 대표유형

[백준 네트워크 연결](https://www.acmicpc.net/problem/1922)

- 부모노드 변경할 때 parents[pa]를 바꿔야하는 거였다. 우앙.
- heapq가 sort,pop보다 시간복잡도가 나쁜 편.
  - heapq 쓰면 좋을 때: 이미 정렬된 리스트에 **원소를 추가할 일**이 생기거나
    새로운 데이터가 추가되어도 정렬이 무조건 유지되어야하는 경우
  - sort,pop : 리스트를 최종적으로 정렬시킬때.
