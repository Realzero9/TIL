# csv 파일 읽기

- csv란?
  - Comma-Separated Values

### 1. 공공 데이터 확인

### 2. 데이터 전처리

- 결측치, 이상치 등 메모장으로 정리

### 3. 편집기 사용하기

- csv 파일 열기 명령어

```
import csv
f = open('seoul.csv', 'r', encoding='utf-8')
data = csv.reader(f, delimiter=',')
for row in data:
	print(row)
f.close()
```

## csv 파일 가공 시 포인트

#### 1. 변수 정하기

#### 2. 초기화 !!!

- 조건에 따라 변할 값도 최적화 하기

#### 3. 자료형 확인하기

#### 4. 조건 만족할 때 재입력 시키기