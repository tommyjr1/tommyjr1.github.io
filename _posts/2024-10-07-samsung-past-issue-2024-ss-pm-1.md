---
title: 2024 삼성 상반기 오후 1번 - 마법의 숲 탐색
date: 2024-10-09T08:42:34.185Z
tags:
  - BFS
  - Python
  - 맵 탐색
categories:
  - PS
description: null
slug: null
lastmod: null
sitemap:
  changefreq: ""
  priority: 0
---
뭐 이딴 문제가 다있어ㅠㅠ
1. 남쪽으로 끝까지 내려가는 함수 필요. -> move()
2. 더이상 내려가지 못할때, 다른 정령 타고갈 수 있는지 알아야함. 
<br> -> 생각이 잘못된거임. 더이상 내려가지 못한다? 그럼 골렘은 고정됨. 이제 정령 안에서 움직이던 타고 넘어가던 그 끝은 결과값임. 알고말고가 아니라 계산을 해야지... bfs였던 것.
3. 정령이 있는 곳의 맵을 정렬 id로 채워둬야할거같음.?

<-->
1. 저 canGo에 대한 발상이,, 굳이 저기가 다 비어있지않아도되는거아닌가?
아 이해함. 결국 움직이면 남쪽으로 한칸 내려가야하니까, 만약 y,x로 내려가야하는거면 y-1, x에서도 가능하고 y,x에서도 가능해야하는것. 회전하는 경우에 만약 처음에 서쪽으로 움직이는 게 어려웠다? y-1,x 되는지 검사할때부터 False인것임.. 이걸 어떻게 생각하는거지. 시뮬인데 시뮬이 아니잖아 이건ㅠㅠ
2. 골렘의 출구는 따로 저장해둬도 된다.
3. bfs 오랜만. deque()쓰는거. 재귀아님. q에 일단 다 넣고 다 확인하면서 보는거. 그게 bfs.
4. 골렘 움직이게 할때, return 값이 없어도되고, return값을 굳이 움직이는 함수에서 계산안해도됨. global answer에다 더해도되잖앙.
5. map 사이즈 작으면 max로 지정하고, isRange()함수 만드는게 나음.


```py
MAX_L = 70
R,C,K = 0.0.0 # 이렇게하고 main에서 global로 두면 좋음.
dx = [0,1,0,-1]
dy = [-1,0,1,0]
#dx, dy 따로 나누는게 훨씬 편하다
f = [[0]*(MAX_L) for _ in range(MAX_L+3)] # 여기서 [3-R+2][0-C-1]사용. 이럴거면 필요한 것 -> inRange()
isExit = [[False]*(MAX_L) for _ in range(MAX_L+3)] 
answer=0

def inRange(y,x):
  return 3<=y<R+3 and 0<=x<C


def checkmove(y,x):
  #가고자하는 중심 좌표가 y,x
  flag = y+1<R+3 and x+1<C and x-1>=0 
  #먼저 y-1, x 증명
  flag = flag and f[y-2][x]==0 #이게 증명되려면 y-2>=3 이어야하는디
  flag = flag and f[y-1][x]==0
  flag = flag and f[y][x]==0
  flag = flag and f[y-1][x-1]==0
  flag = flag and f[y-1][x+1]==0
  #y,x 가능한지
  flag = flag and f[y-1][x]==0
  flag = flag and f[y][x]==0
  flag = flag and f[y+1][x]==0
  flag = flag and f[y][x-1]==0
  flag = flag and f[y][x+1]==0
  return flag

#왜 bfs인가 생각해보니, 이게 어느방향으로 튈지모름. 모든 경우 고려하면서 제일 높은값 가야함.
def bfs(y,x):
  result = y
  q = deque([])
  q.append((y,x))
  visited = [[False]*C for i in range(R+3)]
  visited[y][x]=True

  while q:
    y,x = q.popleft()
    for i in range(4):
      ny, nx = y+dy[i], x+dx[i]
      #ny, nx가 골렘 내부이거나, 골렘외부인데 y,x가 출구이거나+ny,nx에 골렘이 있어야함^^;
      if inRange(ny, nx) and not visited[ny][nx] and (f[ny][nx]==f[y][x] or (isExit[y][x] and f[ny][nx]!=0)):
        q.append((ny,nx))
        visited[ny][nx]=True
        result = max(result, ny)
  return result


def move(x, y, d, k):
  golem = (x, y, d)
  #남쪽으로 움직이기
  if checkMove(y+1, x):
    move(y+1, x, d, k)
  elif checkMove(y+1, x-1):
    move(y+1, x-1, (d+3)%4, k)
  elif checkMove(y+1, x+1):
    move(y+1, x+1, (d+1)%4, k)
  else:
    #다 못움직이는 경우. 
    #먼저 골렘전체가 내부에 있는지 봐야함.
    if not inRange(y-1,x-1) or not inRange(y+1, x+1):
      resetMap()
    else:
      #정령 내부에서 움직이기. => 여기가 마지막 움직임이니까, 여기서 결과값을 받아야함.
      #또한 골렘도 이제 안움직임. 여기 고정인거임.
      f[y][x]=k
      for i in range(4):
        f[y+dy[i]][x+dx[i]]=k
        #와우 이런 멋진
      #골렘 출구도 여기에 기록해줌.
      isExit[y+dy[d]][x+dx[d]]=True
      #아 함수 안에서 정답 계산하려면 이렇게하면되는구나.
      global answer
      answer += bfs(y,x) -3 +1 # 계산 유의.


if __name__ =="__main__":
  global R,C,K
  R, C, K = map(int, input().split())
  result=0
  for k in range(1,K+1):
    c, d = map(int, input().split())
    move(k,1,c,d,)
  print(answer)

```