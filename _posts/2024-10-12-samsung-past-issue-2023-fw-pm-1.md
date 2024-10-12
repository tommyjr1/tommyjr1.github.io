---
title: 2023 삼성 하반기 오후 1번 - 루돌프의 반란
date: null
tags: []
categories: []
description: null
slug: null
lastmod: null
sitemap:
  changefreq: ""
  priority: 0
---

```py
MAX_N=50
N,M,P,C,D = 0,0,0,0,0
map = [[0]*(MAX_N+1) for _ in range(MAX_N+1)]
player = [(0,0)]*MAX_P+1
knocked = [-1]*MAX_P+1
isDead [False]*MAX_P+1

def onMap(id, r,c,):
  global player
  player[id] = (r,c)
  map[r][c] = id

def inRange(r,c):
  if not 1<=r<N+1 or not 1<=c<N+1:
    return False
  return True

# def isAlive(m,p):
#   #좌표 확인
#   r,c = player[p]
#   return inRange(r,c)

def isKnocked(m,p):
  #m턴에 기절인지 확인
  if knocked[p]>=m-1:
    return True
  return False

pq = []

def getDist(r1,r2,c1,c2):
  return (r1-r2)*(r1-r2) + (c1-c2)*(c1-c2)

def findSanta(m,r,c):
  # 우선순위 생각했는데 너무 비효율?
  minSanta = -1
  #와 우선순위 많을때 이렇게 tuple만들면 이대로 비교한다..... 작을수록 좋으니까저건 마이너스
  mindistSanta = (INF, -r, -c)
  for i in range(P):
    if not idDead[i]:
      sr,sc = player[i]
      dist = getDist(r,sr,c,sc)
      cmpSanta(dist, -sr, -sc)
      if mindistSanta>cmpSanta:
        mindistSanta = cmpSanta
        minSanta = i
  return minSanta

dr = [-1,0,1,0,1,-1,1,1,-1]
dc = [0, 1,0,-1,1,1,-1,-1]

def findway(point, target):
  pr, pc = player[point]
  tr, tc = player[target]

  # 8방향은 이거다,,
  mr=0
  if tr>pr:
    mr=+1
  elif tr<pr:
    mr=-1
  mc=0
  if tc>pc:
    mc=1
  elif tc<pc:
    mc=-1

    return mr, mc


def interact(newSanta,d):
  r,c = player[newSanta]
  if crashedSanta !=-1:
    nr, nc = r+dr[d], c+dc[d]
    player[crashedSanta] = (nr, nc)
    interact(crashedSanta,d)

def interact(r,c,mr,mc):
  if 
  player[new]=(r,c)
  crashedSanta = map[r][c]
  if crashedSanta !=-1:
    nr, nc = r+dr[d], c+dc[d]
    if inRange(nr, nc):
      player[crashedSanta] = (nr, nc)
      interact(crashedSanta,nr, nc, d)
  map[r][c] = new

def rudopohCrash(cr,cc,mr,mc):
  # 루돌프가 박치기. 루돌프가 움직인 방향으로 밀림
  mover = map[cr][cc]
  nr, nc = mr*C+cr, mc*C+cc
  player[mover] = (nr,nc)
  map[cr][cc]=0
  interact(nr, nc, mr,mc)

# 이런식으로 변수를 많이 줘야하면, 함수 안에 while 문으로 넣어도 문제가 없다. 이 문제 모범답안?에는 while문 파티임..
def santaCrash(crasher, cr,cc,mr,mc)
    mover = crasher
    nr, nc = -mr*D+cr, -mc*D+cc
    player[mover] = (nr,nc)
    interact(nr, nc, -mr,-mc)

def rMove(m):
  r,c = player[0]
  santa = findSanta(r,c)
  if santa==-1:
    # 산타가 다 Out됨. 게임 종료
    return 
  mr, mc = findway(0,santa)
  #존재하는 산타쪽으로 움직이는거라 루돌프가 밖으로 나갈일은 없다.
  nr, nc = r+mr, c+mc
  player[0]=(nr,nc)
  #움직일때 중요한것 중 하나 -> 이전 좌표 초기화
  map[r][c]=-1
  rudolphCrash(nr,nc, mr, mc)
  
  #움직이고 충돌인지 확인
  #충돌했다면 산타 상호작용 연속적
  #그리고 산타 기절

def sMove():

  #움직이고 충돌인지 확인
  #충돌했다면 산타 상호작용 연속적
  #그리고 산타 기절


def play(m):
  #루돌프 움직임
  rMove(m)
  for p in range(P):
    if isAlive(m,p):
      #산타 움직임
      sMove(m,p)
  


def main():
  global N,M,P,C,D
  N,M,P,C,D = map(int, input().split())
  Rr, Rc = map(int, input().split())
  onMap(0,Rr, Rc)
  for p in range(P):
    pid, Sr, Sc = map(int, input().split())
    onMap(pid, Sr, Sc)
  for m in range(1, M+1):
    play(m)


```