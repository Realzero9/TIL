# 유용한 표준 라이브러리

## 내장함수

- 기본 입출력 함수, 정렬함수
  - sum()
  - min()/max()
  - eval(): 식의 계산
  - sorted()
  - sorted() with key: lambda 함수 넣어서 구현

## itertools

- 반복되는 형태의 데이터 처리
- 순열(P) 라이브러리: 순서 상관 있음
  - from itertools import permutations
- 조합(C) 라이브러리: 순서 상관 없음
  - from itertools import combinations
- 중복순열
  - from itertools import product
- 중복조합
  - from itertools import combinations_with_replacement

## heapq

- 우선순위 큐 기능 구현에 사용

## bisect

- 이진탐색기능(Binary Search)

## collections

- 덱(deque)
- 카운터(Counter): Word Cloud 만들때 사용되는 라이브러리
  - from collections import Counter
  - 리스트(iterable) 객체에서 내부의 원소가 등장한 횟수 셈

## math

- 필수 수학적 기능
- gcd(): 최대공약수
- lcm(): 최소공배수
  - return a*b // math.gcd(a,b)

