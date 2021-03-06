# 소수

1보다 큰 자연수 중에서 1과 자기자신을 제외한 자연수로는 나누어 떨어지지 않는 자연수

## 성능

- 2부터 x-1까지의 모든 자연수에 대하여 연산 수행
- 시간복잡도: O(X) (모든 수를 하나씩 확인함)



## 약수의 성질

- 모든 약수가 가운데 약수를 기준으로 곱셈 연산에 대해 대칭을 이룸
- 따라서 가운데 약수(제곱근)까지만 확인하면 됨

## 개선된 알고리즘 성능

- 2부터 x의 제곱근까지 모든 자연수에 대하여 연산 수행
- 시간복잡도: O(N^1/2)



## 다수의 소수 판별

### 에라토스테네스의 체 알고리즘

- 다수의 자연수에 대하여 소수여부를 판별할때 사용
- N보다 작거나 같은 모든 소수를 찾을 때 사용

### 동작과정

1. 2부터 N가지의 모든 자연수 나열
2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i 찾기
3. 남은 수 중에서 i의 배수를 모두 제거 (i는 제거하지 않음)
4. 반복안될 때까지 2,3번 과정 반복

### 성능

- 시간복잡도: O(NloglogN)
- 다수의 소수를 찾는 문제에서 효과적
- 각 자연수에 대한 소수여부를 저장해야하여 메모리가 많이 필요함