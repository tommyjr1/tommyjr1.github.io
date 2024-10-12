---
title: 2023 삼성기출 하반기 오전 1번 - 왕실의 기사 대결
date: 2024-10-12T14:12:29.160Z
tags:
  - BFS
  - 맵 탐색
categories:
  - PS
description: null
slug: null
lastmod: null
sitemap:
  changefreq: daily
  priority: 1
---
오전오후는 문제가 비슷한것도 같다,,?

이번에는 pycharm에서 풀어볼게,,

내가 풀었다,,,

```py
from collections import deque
import sys
input = sys.stdin.readline

#왕실의 기사 대결

MAX_L = 40
MAX_N = 31
L,N,Q = 0,0,0
board = []
kmap = []
isDead = [False for _ in range(MAX_L+1)]
class Knight:
    def __init__(self,r,c,h,w,k):
        # self.id=id
        self.r=r
        self.c=c
        self.h=h
        self.w=w
        self.k=k
        self.dam=0
    def getendr(self):
        return self.r+self.h
    def getendc(self):
        return self.c+self.w
    def checkDamage(self):
        for r in range(self.r, self.r+self.h):
            for c in range(self.c, self.c+self.w):
                if board[r][c]==1:
                    self.dam+=1
        return self.k-self.dam
    def fill(self,n):
        global kmap
        for r in range(self.r, self.r+self.h):
            for c in range(self.c, self.c+self.w):
                kmap[r][c]=n
    def clear(self):
        global kmap
        for r in range(self.r, self.r + self.h):
            for c in range(self.c, self.c + self.w):
                kmap[r][c] = 0

knightlist=[[0] for _ in range(MAX_N+1)]

def inRange(r,c):
    if 1<=r<=L and 1<=c<=L:
        return True
    return False

dr = [-1,0,1,0]
dc = [0,1,0,-1]
def play(i,d):
    global kmap
    if isDead[i]:
        return
    q = deque()
    q.append(i)
    visited = [False for _ in range(MAX_N+1)]
    visited[i]=True
    mr, mc = dr[d], dc[d]

    while q:
        ci = q.popleft()
        ck = knightlist[ci]
        cr,cc = ck.r, ck.c
        endr, endc = ck.getendr(), ck.getendc()
        for r in range(cr+mr, endr+mr):
            for c in range(cc+mc, endc+mc):
                if not inRange(r,c):
                    return
                if board[r][c]==2:
                    return
                kid = kmap[r][c]
                if kid!=0 and kid!=ci and not visited[kid]:
                    visited[kid]=True
                    q.append(kid)
    kmap = [[0]*(L+1) for _ in range(L+1)]
    for n in range(1,N+1):
        if isDead[n]:
            continue
        if visited[n]:
            knightlist[n].r, knightlist[n].c = knightlist[n].r+mr, knightlist[n].c+mc
            if n!=i:
                if knightlist[n].checkDamage()<=0:
                    isDead[n]=True
                    continue
        knightlist[n].fill(n)




    moveR, moveC = dr[d], dc[d]
    #움직이는 칸 확인
def addKnight(n, args):
    global knightlist
    r, c, h, w, k = args
    temp = Knight(r, c, h, w, k)
    temp.fill(n)
    knightlist[n] = temp

def main():
    global L,N,Q
    global board, kmap
    L,N,Q = map(int, input().split())
    kmap = [[0]*(L+1) for _ in range(L+1)]
    board.append([0]*(L+1))
    for l in range(L):
        temp = list(map(int, input().split()))
        board.append([0]+temp)



    for n in range(1,N+1):
        args = list(map(int, input().split()))
        addKnight(n,args)



    for q in range(Q):
        i,d = map(int, input().split())
        play(i,d)

    ans=0
    for i in range(1,N+1):
        if not isDead[i]:
            ans += knightlist[i].dam
    print(ans)

if __name__=="__main__":
    main()
```