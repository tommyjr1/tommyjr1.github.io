---
title: 2024 삼성 상반기 오전 2번 - 코드트리 투어
date: null
tags:
  - Dijkstra
  - 그래프 탐색
  - heapq
categories:
  - PS
description: 2024-10-12T01:43:35.068Z
slug: null
lastmod: null
sitemap:
  changefreq: daily
  priority: 1
---
5번에서 전체의 시작점이 바뀔수 있다. 이부분이 일단 lazy 계산 필요한거 확인.

간선이 노드보다 많다.

```py
MAXNODE = 2001
MAXLINE = 10001
INF = float('inf')  # 무한대 값을 정의합니다.

revList = [[(0,0)]*30001]
start = 0



N, M = 0, 0  # 도시의 개수 N과 간선의 개수 M을 초기화합니다.
D = []  # 다익스트라 알고리즘을 통해 시작도시부터 각 도시까지의 최단경로를 저장합니다.

class Package():
  def __init__(self, id, rev, dest, profit):
    self.id = id
    self.rev = rev
    self.dest = dest
    self.profit=profit

  def __lt__(self, other):
    #정렬 기준도 이렇게 만들고,,
    # 저번에 add는 함수 합쳐야할때쓴것처럼, 지금은 비교한 리스트가 필요하니까.
    # lt로 한 이유는, heapq 작은게 맨앞임. lt에서 제일 less해야 높은 우선순위.

    if self.profit == other.profit:
      return self.id < other.id # 이게 True면 id 작은게 더 높은 우선순위?
    return self.profit> other.profit # 우선순위 profit클수록 높음. 이게 True 리턴하면 지가 더 높은 우선순위



def create(n,m,arr):
  global A,N,M
  N,M = n,m
  A = [[INF]*N for _ in range(N)] # 이중행렬을 만드는구나 그냥. 간선이 많으니까 이렇게하면 안에 다 저장해야할줄알았더니,,, 아래에서 그냥 제일 작은애로 넣음,,,똑똑한데...
  for i in range(N):
    A[i][i]=0 #자신에게 가는 비용.
  for i in range(M):
    u,v,w = arr[i*3], arr[3*i+1], arr[3*i+2]
    A[u][v] = min(A[u][v], w) # 아 어차피 길이가 긴 애는 안쓰니까. 하나만 저장하면됨. 멍청
    A[v][u] = min(A[v][u], w)


def addPackage(i, rev, dest):
  # 여기서 바로 이윤계산 해둬야함!!!!!!!!!
  profit = rev - D[dest]
  #다익스트라로 최소비용 계산 != 우선순위에 맞게 상품 배열.
  # 여기서 상품배열 시작.
  heapq.heappush(pq, Package(i, rev, dest, profit))
  # 이 기준은? Package 클래스에 지정. 그리고 이게 노드지도랑은 또 다른거임. 이걸로 내가 노드도 저장하고 여행상품으로도 저장하고 막 이럴라했던것도 문제다.
  isMade[i] = True  
# 계산해야하는게 두개. 최단거리. 최종 가치.
# 최단거리를 다익스트라로 구함
# 아 내가 노드가 추가된다고 생각했구나? 노드는 추가가 안됨!!!!! 평생 지도는 유지!!!!!!!!
# 노드 추가없으니까 시작점만 있으면 최단거리는 고정..
# 시작점 바뀔때만 계산하면 되는게 맞네,,,
def dijkstra():
  #이게 진자 다익스트라네
  global D
  D = [INF]*N
  visited = [INF]*N
  # 본인만 0
  D[start]=0

  #dijkstra. two for loop.
  for _ in range(N):
    #1. get a node's id with the smallest dist. 
    #gonna be the start node as a start 
    v=-1
    minDist=INF
    for j in range(N):
      if not visited[j] and minDist>D[j]:
        v=j
        #우리는 최소값이 필요. 그래서 비교문 보면. minDist가 더 큰지를 확인함. 더 크면 minDist에 D[j]값을 넣어야하니까.
        minDist = D[j]
    if v==-1:
      break
    # now you got the start. v=start.
    visit[v]=True
    # now you update the shortest distance 
    for j in range(N):
      if nodes[v][j] != INF and D[j]>D[v]+A[v][j]:
        D[j]=D[v]+A[v][j]



def bestVal():
  while pq:
    p = pq[0] # 아 pop하면 안되는?
    if p.profit<0:
      # 아미친 상품이 고정되어있는게아니라 팔아버리는거구나,,
      # 안팔거면 pop 안해야함ㄷㄷ
      break    
    heapq.heappop(pq)
    if not isCancel[p.id]:
      return p.id
  return -1  

pq = []

def update(param):
  global start
  start = param
  dijkstra()
  temp_pack=[]
  while pq:
    temp_pack.append(heapq.heappop(pq))
  # 이렇게 pq 비우고 다시 profit계산해서 pq에 넣음.
  for p in temp_pack:
    addPackage(p.id, p.rev, p.dest)

def main():
  Q = int(input())
  for q in range(Q):
    args = list(map(int, input().split()))
    cmd = args[0]
    if cmd==100:
      create(args[1],args[2], args[3:])
      dijkstra() # 어차피 노드는 여기서 고정이니까ㅠㅠ ㅠ ㅠ 노드가 추가되는줄 알았던 멍청한 사람.
    elif cmd==200:
      i, rev, dest = args[1:]
      addPackage(i,rev,dest)
       
    elif cmd==300:
      i = args[1]
      # 내가 이렇게햇던게, 막 상품을 리스트로 받아야하나? id로 정렬해야하나? 고민했다가 id로 정렬하는걸 생각해버렸음. 생각은 맞는데 결국 틀림.
      # 이렇게 revList[i] = (0,0) 대신
      if isMade[i]:
        isCancel[i]=True
      # 만들었다 따로, 지웠다 따로.
      # 그리고 상품 자체는 heaqp에 수익 순으로 저장. 빡세네..
    elif cmd==400:
      bestVal()
    elif cmd==500:
      change = args[1]
      update(change)


```
