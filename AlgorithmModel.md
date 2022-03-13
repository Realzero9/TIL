# 알고리즘 모델학습

## CNN (Convolution Neural Network)

- 이미지의 공간정보 유지 및 학습
  - 각 Layer의 입출력데이터 형상 유지
  - 복수 필터 사용 (추출 및 학습)
  - Pooling Layer (수집 및 강화)
  - 필터: 공유파라미터 (학습파라미터가 적음)

- Fully-Connected Layer
  - Input 데이터: 1차원
  - 사진데이터: 1차원으로 변환
    - 한계: 공간정보 손실 > 특징추출 및 학습이 비효율적

### Feature Extraction & Classification

- 특징추출(Feature Extraction)
  - Convolution Layer + Pooling Layer 반복
    - Convolution Layer: Input 데이터에 필터 적용, 활성화함수 반영
    - Pooling Layer: (선택적)
- 클래스분류(Classification)
  - Flatten Layer + Fully-connected Layer
    - Flatten Layer: 이미지데이터 > 배열형태
    - Fully-connected Layer: 배열화된 이미지데이터 분류

### 주요용어

- 합성곱(Convolution) - 필터가 한번 거친 출력(Activation Map까지 얻는 과정) [반복가능]
- 채널(Channel) - Feature Map의 n개 Filter (컬러이미지=각 픽셀을 3개 실수로 표현한 3차원 텐서)
- 필터(Filter) - 부분, 정사각형 행렬(공용파라미터), CNN의 학습대상
- 커널(Kernel) - Filter
- 스트라이드(Stride) - 옮기는 양
- 패딩(Padding) - Convolution결과 데이터 손실을 막기위해 Zero(0)를 입혀주는 것(노이즈발생)
- 피처맵(Feature Map) - Input 데이터(*Channel) + (n개)Filter의 Convolution 결과(channel의 합)
- 액티베이션맵(Activation Map) - Convolution Layer(Filter의 출력) * Filter 수 + 활성함수 적용
- 풀링레이어(Pooling Layer) - Convolution Layer의 resize로 새 Layer 얻기(Max/Min) [크기감소]
  - 오버피팅 방지