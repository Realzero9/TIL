# 위상정렬

- 사이클이 없는 방향그래프(DAG)의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것
- 진입차수(Indegree): 특정한 노드로 들어오는 간선의 개수
- 진출차수(Outdegree): 특정한 노드에서 나가는 간선의 개수

## 동작과정

1. 진입차수가 0인 모든 노드를 큐에 넣는다
2. 큐가 빌때까지 다음 과정을 반복
   1. 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거
   2. 새롭게 진입차수가 0이 된 노드를 큐에 넣음

- 결과적으로 각 노드가 큐에 들어온 순서가 위상정렬을 수행한 결과

## 특징

- DAG(Direct Acyclic Graph): 순환하지 않는 방향그래프 에 대해서만 수행 가능
- 여러 답이 존재할 수 있음
- 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재
- 스택을 활용한 DFS로 위상정렬 수행도 가능

## 성능

- 시간복잡도: O(V+E)
- 차례대로 모든 노드를 확인하며 각 노드에서 나가는 간선을 차례대로 제거