# 투포인터

- Two Pointers
- 리스트에 순차적으로 접근해야 할 때 두개의 점의 위치를 기록하면서 처리
- 시작점과 끝점 2개의 점으로 데이터의 범위 표현

## [문제] 특정합을 가지는 부분연속수열 찾기

- 해결
  1. 시작점과 끝점이 첫번째 원소의 인덱스(0)을 가리키도록 함
  2. 현재 부분합이 M과 같다면 카운트
  3. 현재 부분합이 M보다 작다면 end 1증가
  4. 현재 부분합이 M보다 크거나 같다면, start 1증가
  5. 모든 경우를 확인할 때까지 2번부터 4번까지의 과정 반복

# 구간합

- Interval Sum
- 연속적으로 나열된 n개의 수가 있을때 특정 구간의 모든 수를 합한 값을 계산

## 접두사 합

- Prefix Sum
- 배열의 맨 앞부터 특정위치까지의 합을 미리 구해놓은 것
- 구간합 구할때 일종의 cache처럼 활용