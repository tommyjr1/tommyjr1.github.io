---
title: "TIL: 코드트리 오마카세 "
date: 2024-04-13T17:45:51.520Z
tags:
  - TIL
  - Python
categories:
  - PS
lastmod: 2024-04-13T17:45:55.210Z
sitemap:
  changefreq: daily
  priority: 1
---

## 내가 구현한 코드. -> 시간초과

내 제일 큰 문제는, 내가 출력해야 하는 값에 집중한게 아니라, 그 과정을 하나하나 돌리고 있었다는 것.<br>
내가 정말 수학적 사고가 부족한 것 같다.<br>
그래도 잘한 건 해시테이블..

```py

# 0. 초밥 이동 함수
#모든 초밥의 존재하는 위치를 더해줘야함
def sushi_move(t):
    global sushiList
    for name in sushiList.keys():
        sushiList[name] = list(map(lambda x: (x+1)%L, sushiList[name]))



# 1. 초밥 넣는 함수
#초밥이름: 존재하는 위치.
def sushi_add(t,x,name):
    global sushiList
    global sushiCnt
    if name in sushiList:
        sushiList[name]+=[x]
    else:
        sushiList[name]=[x]
    sushiCnt+=1



# 손님 입장 함수?
# 좌표에 손님 들어온 것으로 처리
def customer_in(x,name,n):
    global customerList
    global customerCnt
    customerList[name] = [x, n]
    customerCnt+=1

#
# 초밥 먹는 함수
# 손님들이 자기 앞에있는 초밥 먹기.
# n개 먹었으면 손님 퇴장처리.
def customer_eat(t):
    global sushiList
    global customerList
    global sushiCnt
    global customerCnt

    temp = customerList.copy()

    #고객별로 확인
    for name, (place, n) in customerList.items():
        cnt = n
        # 이 사람의 초밥
        sushisPlate = sushiList[name]
        # print('plate', sushisPlate)
        if place in sushisPlate:
            sushis = sushisPlate.count(place)

            cnt-=sushis
            sushiCnt-=sushis
            sushiList[name] = [s for s in sushisPlate if s != place]
            # print('eat', sushiList)
            if cnt>0:
                temp[name] = [place, cnt]
            else:
                temp.pop(name)
                customerCnt-=1

    customerList = temp





# 사진 찍는 함수
def picture(t):
    print(customerCnt, sushiCnt, sep=' ')




if __name__ == "__main__":
    L,Q = map(int, input().split(' '))
    sushiList=dict()
    sushiCnt = 0
    customerList = dict()
    customerCnt =0
    prevTime=0
    while Q>0:
        line = input().split(' ')
        msg = line[0]
        t = int(line[1])
        while t - prevTime>1:
            if sushiCnt>0:
                sushi_move(prevTime+1)
                if customerCnt>0:
                    customer_eat(prevTime+1)
                prevTime+=1
            else:
                prevTime=t-1
        if msg=='100':
            x, name = line[2:]
            x = int(x)
            sushi_move(t)
            sushi_add(t,x,name)
            customer_eat(t)
        if msg=='200':
            x, name, n = line[2:]
            x, n = map(int, [x,n])
            sushi_move(t)
            customer_in(x,name,n)
            customer_eat(t)
        if msg=='300':
            sushi_move(t)
            customer_eat(t)
            picture(t)
        prevTime=t
        Q-=1

```

## 대표 답안

0. 초밥의 위치가 중요한게 아니라, 그래서 사람이 아직 있는지, 아직 안나갔는지, 초밥 먹었는지 이게 중요한거였다.
1. 클래스 만드는 거 오랜만에 본다 굳.
2. 사람이 퇴장하는 시간을 세는 이 파트가 내가 제일 궁금했던 건데,

```py
#사람 입장 시 위치
# 초밥 입장 위치 + 지금까지 지나간 시간 % L
t_sushi_x = (q.x + (entry_time[name] - q.t)) % L

# 입장 후 만나는데 걸리는 시간
# 사람 위치-입장 시 초밥위치 +L % L
additionl_time = (position[name] - t_sushi_x + L) % L
```

3. 이렇게 추가적으로 쿼리를 만들면, 난 초밥 위치를 계속 뺑뺑 돌리는게 아니라 수학적으로 계산해 낼 수 있다.

```py
# 변수 선언
L, Q = 0, 0

class Query:
    def __init__(self, cmd, t, x, name, n):
        self.cmd = cmd
        self.t = t
        self.x = x
        self.name = name
        self.n = n

# 명령들을 관리합니다.
queries = []

# 등장한 사람 목록을 관리합니다.
names = set()

# 각 사람마다 주어진 초밥 명령만을 관리합니다.
p_queries = {}

# 각 사람마다 입장 시간을 관리합니다.
entry_time = {}

# 각 손님의 위치를 관리합니다.
position = {}

# 각 사람마다 퇴장 시간을 관리합니다.
exit_time = {}

# Query를 (t, cmd) 순으로 정렬합니다.
def cmp(q1, q2):
    if q1.t != q2.t:
        return q1.t < q2.t
    return q1.cmd < q2.cmd

# 입력:
L, Q = map(int, input().split())
for _ in range(Q):
    command = input().split()
    cmd, t, x, n = -1, -1, -1, -1
    name = ""
    cmd = int(command[0])
    if cmd == 100:
        t, x, name = command[1:]
        t, x = map(int, [t, x])
    elif cmd == 200:
        t, x, name, n = command[1:]
        t, x, n = map(int, [t, x, n])
    else:
        t = int(command[1])

    queries.append(Query(cmd, t, x, name, n))

    # 사람별 주어진 초밥 목록을 관리합니다.
    if cmd == 100:
        if name not in p_queries:
            p_queries[name] = []
        p_queries[name].append(Query(cmd, t, x, name, n))
    # 손님이 입장한 시간과 위치를 관리합니다.
    elif cmd == 200:
        names.add(name)
        entry_time[name] = t
        position[name] = x

# 각 사람마다 자신의 이름이 적힌 조합을 언제 먹게 되는지를 계산하여 해당 정보를 기존 Query에 추가합니다. (111번 쿼리)
for name in names:
    # 해당 사람의 퇴장 시간을 관리합니다.
    # 이는 마지막으로 먹는 초밥 시간 중 가장 늦은 시간이 됩니다.
    exit_time[name] = 0

    for q in p_queries[name]:
        # 만약 초밥이 사람이 등장하기 전에 미리 주어진 상황이라면
        time_to_removed = 0
        if q.t < entry_time[name]:
            # entry_time때의 스시 위치를 구합니다.
            t_sushi_x = (q.x + (entry_time[name] - q.t)) % L
            # 몇 초가 더 지나야 만나는지를 계산합니다.
            additionl_time = (position[name] - t_sushi_x + L) % L

            time_to_removed = entry_time[name] + additionl_time
        # 초밥이 사람이 등장한 이후에 주어졌다면
        else:
            # 몇 초가 더 지나야 만나는지를 계산합니다.
            additionl_time = (position[name] - q.x + L) % L
            time_to_removed = q.t + additionl_time

        # 초밥이 사라지는 시간 중 가장 늦은 시간을 업데이트 합니다.
        exit_time[name] = max(exit_time[name], time_to_removed)

        # 초밥이 사라지는 111번 쿼리를 추가합니다.
        queries.append(Query(111, time_to_removed, -1, name, -1))

# 사람마다 초밥을 마지막으로 먹은 시간 t를 계산하여 그 사람이 해당 t 때 코드트리 오마카세를 떠났다는 Query를 추가합니다. (222번 쿼리)
for name in names:
    queries.append(Query(222, exit_time[name], -1, name, -1))

# 전체 Query를 시간순으로 정렬하되 t가 일치한다면 문제 조건상 사진 촬영에 해당하는 300이 가장 늦게 나오도록 cmd 순으로 오름차순 정렬을 합니다.
# 이후 순서대로 보면서 사람, 초밥 수를 count하다가 300이 나오면 현재 사람, 초밥 수를 출력합니다.
queries.sort(key=lambda q: (q.t, q.cmd))

people_num, sushi_num = 0, 0
for i in range(len(queries)):
    if queries[i].cmd == 100:  # 초밥 추가
        sushi_num += 1
    elif queries[i].cmd == 111:  # 초밥 제거
        sushi_num -= 1
    elif queries[i].cmd == 200:  # 사람 추가
        people_num += 1
    elif queries[i].cmd == 222:  # 사람 제거
        people_num -= 1
    else:  # 사진 촬영시 답을 출력하면 됩니다.
        print(people_num, sushi_num)
```
