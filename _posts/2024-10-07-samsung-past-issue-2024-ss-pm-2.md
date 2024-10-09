---
title: 2024 삼성 상반기 오후 2번 - 색깔 트리
date: 2024-10-07T01:46:48.341Z
tags:
  - TIL
  - 그래프 탐색
categories:
  - PS
description: null
slug: null
lastmod: null
sitemap:
  changefreq: daily
  priority: 1
---

이거 문제가 너무 어려운데 하고보니 B형인거군요. <br>
다음엔 A형부터 차근차근 해나가야겠어요.

코드트리 모범답안 클론코딩하면서 써봄.

- 직관
**이거 오마카세랑 다를게 없었음.** 매 순간을 구현하는 단순한게 아님.<br>
계속 노드 타고내려가서 바꿔주고 그냥 색 갯수 하나씩 세지뭐 -> 노드 전체를 매순간 탐색하겠다? 뭔가 시간복잡도 out.

**색을 바꾸기도하고, 가치도 색으로 계산 -> 색을 잘 관리하는게 문제 포인트.**

노드의 색, 색 변경 시점을 효율적으로 관리한다 = 모든 노드를 변경하는게 아니라, **나중에 색 알려달라고 할때만 슥 계산할 수 있게 한다.**

가치계산도 동일. 즉 원할때만 계산할 수 있도록, 색 가짓수를 세는 알고리즘 필요.
---
- 알고리즘
색 변경할때마다 시점을 저장 => 나중에 계산할때 써먹을 수 있다. how???<br>
answer : 색 조회할 때, 현재노드에서 루트까지 올라간 후 내려오면서 가장 최신의 색 변경시점을 찾아서 그 값을 주면 된다. 
<br>!!!!아!!!! 변경시점이 제일 큰 애의 색을 기억하면 되는구나.. 한번에 다 바꾼다는 규칙의 포인트. 바꾸는애의 시점과 색만 기억하면 된다..

점수조회할때 => 루트부터 시작해서, 자식노드들 재귀탐색. 






```py
MAXID=10005 #10001에 4는 뭘까,, 
MAXDEPTH = 105
COLORMAX = 5

class Node:
  def __init__(self):
    self.id =0
    self.c=0
    self.lastUpdate=0 # 노드가 추가된 시점. or 마지막으로 색 변경
    self.maxDepth=0
    self.pid=0
    self.childIds=[]


# 점수조회용 클래스. 이걸 클래스로 구현하네? 뭘하는건지 함 보자
class ColorCount:
  def __init__(self):
    self.cnt = [0]*(COLORMAX+1) 
    # 아 색별로 +1하려고 그런거구나!! 갯수 고정이면 리스트길이 고정시켜서 인덱스에 +1 해도되니까.
    # max 값은 저렇게 고정값으로 위에 지정해두는거 ㄱㅊ한거같음

  # add도 함수가 있어요?
  def __add__(self, obj):
    res = ColorCount()
    for i in range(1, COLORMAX+1):
      res.cnt[i] = self.cnt[i] + obj.cnt[i]
    return res 

  #서로다른 색의 개수의 제곱
  def score(self):
    result=0
    for i in range(1, COLORMAX+1):
      result += 1 if self.cnt[i] else 0 # 이건 색이 있으면 1, 아니면 0
    return result * result #왜 가치값을 안주고? 했는데, 어차피 가짓수가지고 값주고, 컬러 리스트는 유지해야함. 자식의 컬러리스트를 __add__하면 이제 내거랑 더해지는거구나. 그럼 score 값도 더하면서 리스트도 갱신해야함.

nodes = [Node() for _ in range(MAXID)]
isRoot = [False]*MAXID

# 해당 노드가 자식노드를 가실 수 있는지 확인하기.
# 루트까지 조상을 각각 탐색하면서 maxDepth 확인해야함.
def canMakeChild(curr, needDepth):
  if curr.id==0:
    # 지금 노드 만든것일때 XXXXX 아님 루트노드의 부모임!!!!!!!!!! 근데 이게 왜 바로 트루를 리턴하지? 
    #-> 만약 여기까지 온거면,curr이 루트일때 아래 조건을 통과한거임. 루트의 maxDepth가 필요 깊이보다 큰거임.
    return True
  if curr.maxDepth <= needDepth:
    # 지금 노드가 가질 수 있는 최대보다 더 많이 필요하면 이제 안되는거지. 이걸 루트까지 올라갈예정.
    return False
  return canMakeChild(nodes[curr.pid], needDepth+1) #나를 만들어야함. 즉 최소 1 필요. 그 다음 부모는 1(지금curr)+1(본인)개 가질수있어야함. 이런 생각이 왜 안굴러가냐고~

# curr 노드의 색 정보와 색이 설정된 시간 리턴.
# 루트에 도달할때까지 부모 타고 몰라가면서 lastUpdate시간 이용해서 노드가 가져야하는 색 계산
def getColor(curr):
  if curr.id==0:
    return 0,0
  parent = getColor(nodes[curr.pid]) # 부모까지 엄청 올라가네. 생각해보면 맨위까지 다 봐야하는게 맞다. 난 왜 중간에서 끊을라한ㄷㄷ
  if parent[1]> curr.lastUpdate: # 위에서 더 마지막에 바꾼게 있음 -> 위에걸 리턴
    return parent
  else return curr.c, curr.lastUpdate
  # 무한 타고올라가기. 이게 재귀지..

# 점수계산하는 함수
def getValue(curr, c, lastUpdate):
  # 루트에서 내려온 색보다, 지금 색 정보가 최신이다?-> 갱신
  if lastUpdate < curr.lastUpdate:
    lastUpdate = curr.lastUpdate
    c = curr.c
  result = [0, ColorCount()] # 최종점수, 컬러팔레트
  result[1].cnt[c]=1
  for childId in curr.childIds:
    child = nodes[childId]
    # 각 자식이 이루는 자식트리의 점수와 color count 값 가져오기.
    subResult = getValue(child, c, lastUpdate)
    result[1] = result[1]+subResult[1] # 아미친 클래스 __add__가 이거용이구나. 그냥 더하면 어케 합칠지 설정해두는거구나,, 세상에....
    result[0]+=subResult[0]
  result[0] +=result[1].score() # 싹 본인 점수만 긁어모아줌.
  return result

if __name__=="__main__":
  Q = int(input())
  for i in range(1, Q+1):
    query = list(map(int, input().split()))
    T = query[0]
    if T==100:
      mid, pid, c, md = query[1:] # 아 이렇게 찢어서 지정할 수 있구낭
      if pid==-1: isRoot[mid]=True
      #지금 자식 만들수 있는지 확인
      if isRoot[mid] or canMakeChild(nodes[pid], 1):
        nodes[mid].id=Id
        nodes[mid].c=c
        nodes[mid].maxDepth=md
        nodes[mid].pid=0 if isRoot[mid] else pid # 엥뭐에요 pid 저장 안하네? -1이라고 맨뒤 리턴하는거 아니구나? -1은 그냥 플래그였음.
        nodes[mid].lastUpdate = i
        if not isRoot[mid]:
          nodes[pid].childIds.append(mid)
      elif T==200:
        mid, c = query[1:]
        # 색 변화명령에 lastUpdate만 갱신. LAZY UPDATE가 가능하도록!!
        # getColor, getValue할때만 lazy 계산이 되도록. 이런걸 lazy 계산이라카는구나
        nodes[mid].c=c
        nodes[mid].lastUpdate=i
      elif T==300:
        mid=query[1:]
        print(getColor(nodes[mid])[0])
      elif T==400:
        value=0
        for ind in range(1, MAXID):
          if isRoot[ind]: # 루트를 찾는거임. 루트부터 해야해서.
            value+=getValue(nodes[ind], nodes[ind].c, nodes[ind].lastUpdate)[0]
        print(value)

```

... 이걸 어케 외워요.
- Lazy 계산을 고려한 구성.
- class 무한 활용.
- 재귀 잘 사용하면됨.
- 문제를,,,문제를 잘 읽자.
