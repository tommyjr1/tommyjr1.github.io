---
title: 2024 삼성 상반기 오전 1번 - 색깔 트리
date: 2024-10-09T09:09:55.318Z
tags: []
categories: []
description: null
slug: null
lastmod: null
sitemap:
  changefreq: daily
  priority: 1
---

- 중심잡고 90도 회전
  - 유물 1차 획득가치 max
    - 회전각도 작은방법
      - 회전 중심좌표의 열이 가장 작은 구간.
        - 열이 같다면 행이 가장 작은 구간.

- 같은 숫자 3개 이상의 덩어리. 가치는 모인 조각 수.
-> bfs? 깊이보단 너비 아닐가

- 유적 채우기
  - 열 번호 작은 순
    - 행 큰 순

- 2차 획득도 가능. 획득. 채우기. 획득. 채우기. 더이상 없을때까지.

- K번의 턴 까지하는데, 그 중 중간에 유물획득이 없으면 종료


```py
# g = [[0]*5 for _ in range(5)]
# ml = [0]*300
# m=[]
answer =0


def rotate(self, sy, sx, cnt):
  result = Board()
  result.a = [row[:] for row in self.a]
  for _ in range(cnt):
      # sy, sx를 좌측상단으로 하여 시계방향 90도 회전합니다.
      tmp = result.a[sy + 0][sx + 2]
      result.a[sy + 0][sx + 2] = result.a[sy + 0][sx + 0]
      result.a[sy + 0][sx + 0] = result.a[sy + 2][sx + 0]
      result.a[sy + 2][sx + 0] = result.a[sy + 2][sx + 2]
      result.a[sy + 2][sx + 2] = tmp
      tmp = result.a[sy + 1][sx + 2]
      result.a[sy + 1][sx + 2] = result.a[sy + 0][sx + 1]
      result.a[sy + 0][sx + 1] = result.a[sy + 1][sx + 0]
      result.a[sy + 1][sx + 0] = result.a[sy + 2][sx + 1]
      result.a[sy + 2][sx + 1] = tmp
  return result

dy = [-1, 0,1,0]
dx = [0,1,0,-1]

def findValue(tmp):
  q = deque([])
  visited = [[False]*5 for _ in range(5)]
  visited[0][0]=True
  val=0

  for y in range(5):
    for x in range(5):
      vals = [[0]*5 for _ in range(5)]
      ans=0
      q.append((y,x))
      while q:
        r,c = q.popleft()
        for d in range(4):
          ny, nx = r+dy[d], c+dx[d]
          if inRange(ny,nx) and not visited[ny][nx] and tmp[ny][nx]==tmp[r][c]:
            ans+=1
            visited[ny][nx]=True
            q.append((ny,nx))
      val+=ans
  return val


def tamsa1(g, ml):
  result=0
  cmp = []
  # 9개의 3*3 그리드 경우의 수
  cl = [(1,1), (1,2) ,(1,3), (2,1), (2,2), (2,3), (3,1), (3,2), (3,3)]
  for y,x in cl
    # 이 안에서 3가지 회전 경우의 수
    for a in [90, 180, 270]:
      tmp = turn(g,y,x,a)
      val = findValue(tmp)
      cmp.append((val, a, x, y))
  cmp_sort = sorted(cmp, key=lambda x: (x[0], -x[1], -x[2], -x[3]), reverse=True)
  
  return cmp_sort[0]



def main():
  K,M = map(int, input().split())
  for i in range(5):
    temp = list(map(int, input().split()))
    g[i]=temp
  ml = list(int, input().split())

  for k in range(K):
    tamsa(g, ml)
  print(answer)
  


  
  

```