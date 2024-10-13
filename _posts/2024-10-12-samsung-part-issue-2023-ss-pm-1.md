---
title: 2023 삼성 상반기 오후 1번
date: 2024-10-12T22:21:07.593Z
tags: []
categories: []
description: null
slug: null
lastmod: null
sitemap:
  changefreq: ""
  priority: 0
---
? 이게 무슨 변태같은 문제임?

```py

MAX_M=10
INF = float('inf')
N,M,K = 0,0,0
maze = []
peoplemaze = []
persons = [0 for _ in range(MAX_M+1)]
isOut = [False for _ in range(MAX_M+1)]
exit = (0,0)
moved = 0


def inRange(r,c):
    if 1<=r<=N and 1<=c<=N:
        return True
    return False










def checkEnd():
    # 한명이라도 false가 있다. return not True => return False
    return not (False in isOut)

dr = [-1,1,0,0]
dc = [0,0,1,-1]
def play():
    global persons
    newpersons=[0 for _ in range(M+1)]
    er,ec = exit

    for m in range(1,M+1):
        r,c = persons[m]
        cdist = abs(r,er)+abs(c,ec)
        mdist=INF
        for d in range(4):
            nr, nc = r+dr[d], c+dc[d]
            dist = abs(nr,er)+abs(nc,ec)
            if cdist>dist and mdist>dist:
                mdist = dist
        if maze[nr][nc]==0:
            newpersons[m]=(nr, nc)
    persons = newpersons

    #거리가 제일 가까운 곳.
    minid=0
    mindist=(INF, INF, INF)
    for m in range(1, M + 1):
        r, c = persons[m]
        cdist = abs(r, er) + abs(c, ec)
        if mindist>(cdist, r, c):
            mindist = (cdist, r, c)
            minid = m

    closest = persons[minid]
    h = closest[0]-er
    w = closest[1]-ec

# # rotate method
# for i in range(d+1):
#     for j in range(d+1):
#         new[r+j][c+d-i] = prev[r+i][c+j]


def main():
    global N,M,K,exit
    global maze, peoplemaze, persons
    N,M,K = map(int, input().split())
    maze.append([0 for _ in range(N+1)])
    peoplemaze = [[0]*(N+1) for _ in range(N+1)]
    persons = [0 for _ in range(M+1)]
    for n in range(N):
        temp = list(map(int, input().split()))
        maze.append([0]+temp)
    for m in range(1,M+1):
        r,c = map(int, input().split())
        persons[m]=(r,c)
        peoplemaze[r][c]=m
    r,c = map(int, input().split())
    exit = (r,c)
    maze[r][c] = -1
    for k in range(1,K+1):
        if checkEnd():
            break
        play()
    print(moved)





if __name__=="__main__":
    main()
```