---
title: 2024 상반기 삼성코테 오전 복기
date: 2024-04-17T06:23:26.466Z
tags:
  - Review
categories:
  - PS
lastmod: 2024-04-17T06:27:12.967Z
sitemap:
  changefreq: daily
  priority: 1
---

나는 1번이랑 2번보고 2번을 먼저 풀었음.<br>
2번이 그냥 스켈레톤 코드가 있길래,,, 시작한 것도 있고,<br>

조건에 "숫자가 매우 클 수 있다." 이러길래,<br>
바로 전날 밤에 푼 오마카세도 숫자가 엄청 컸어서 애먹은 기억에<br>
아 이거 해시테이블로 풀어보면 비빌 만 하겠다 하고 풀었다.<br>

근데 이게 삼성코테 B형 이런거라며,,, ㅇㄴ <br>
조건이 하도 까다로워서 히든케이스에서 에러 백퍼 날 것 같긴함.<br>

2시간반에 다 풀고 1번 돌아가서 보는데 할만해보였음.<br>
빠르게 전체 구조 짜고 함수 다 만들었는데<br>
계속 에러잡다가 끝났댜. 이것도 2시간반 시간 줬으면 풀었을텐데!!

1. 1번 문제는 연구소 문제랑 비슷한 전체 맵 반복확인 + bfs 느낌의 문제.

   - 여기서 배운점은?? 함수를 만들때마다 로그를 찍고 확인하자 제발제발.

   [코드트리 복기 문제](https://www.codetree.ai/training-field/frequent-problems/problems/ancient-ruin-exploration/description?page=1&pageSize=20)

2. 최단거리 다익스트라 + 시간단축 위해서 플래그 전역변수 사용.

   - 테케 10번이 숫자가 커서 안되다가 마지막에 플래그 하나 더 만들어서 해결함.
   - 리스트 안쓰고 다 해시 씀. 굳.
   - 경우의 수 생각하면서, 최단거리를 진자 계산해야하는 경우, 정렬해야하는 경우를 분리해서 플래그를 설정했다.

   [코드트리 복기 문제](https://www.codetree.ai/training-field/frequent-problems/problems/codetree-tour/description?page=1&pageSize=20)
