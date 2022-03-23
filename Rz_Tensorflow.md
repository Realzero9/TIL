# 알고리즘 모델학습

## NN(Neural Network)

- 네트워크 층(Layer)
- 입력데이터/레이블(feature/target)
- 학습피드백(LossFunction)
- 진행방식(Optimizer)

### 데이터처리방식

- 2D 텐서: Fully-Connected Layer / Dense Layer
- 3D 텐서: LSTM / Recurrent Layer (시계열데이터)
- 4D 텐서: 2D합성곱 층(Convolution Layer) (이미지데이터)

### 레이어(Layer)

- 가중치라는 층의 상태를 가짐
- 네트워크가 학습한 지식 [저장가능]
- keras에서는 자동으로  층호환성(Layer compatibility) 맞춰줌
- 얼마나 많은 층을 사용할지, 각 층에 얼마나 많은 은닉유닛을 사용할지 결정해야 함

### 학습피드백: 손실함수 (Loss Function)

- 2개의 클래스 분류 (확률) - 이진 크로스엔트로피(binary_crossentropy)
- 여러개의 클래스 분류 (확률) - 범주형 크로스엔트로피(categorical_crossentropy)
- 회귀 - 평균 제곱 오차(MSE, mean square error)
- 시퀀스(순서있는) 학습 - CTC(Connected Temporal Classification)

### 진행방식: 옵티마이저(Optimizer)

- 확률적 경사 하강법(SGD) - 확률적으로 최소값을 찾는 방법(local minimum을 피하기위해 사용)
- rmsprop - 옵티마이저 기본값

### 분류함수

- Relu - 음수값은 모두 0처리 / 양수값은 x = y
- Sigmoid - 0~1사이의 확률값 표시 / 기준값 0.5 설정하면 두 값으로 나눠줌
- Softmax - 다중확률분포 표시 / 다 더하면 1

### 모델링

- 중간층 유닛이 충분히 커야함 (작으면 정보손실이 생김)
  - Sequential(직관적)
  - API(함수적)

### 컴파일(Compile)

- Optimizer(옵티마이저) + Loss(손실함수) + Metrics(측정지표)

### 학습(fit)

- feature + label, batch_size(처리량), epochs(반복)
- History 객체 반환(딕셔너리)

---



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
  - Filter가 각 픽셀을 1회만 연산한 결과 출력
  - 학습파라미터 없음
  - 행렬 크기 감소, 채널수 변경 없음
  - 오버피팅 방지

### 결론

- CNN은 학습파라미터 수가 매우 적어서, 학습이 쉽고 처리속도가 빠르다

---



## Transfer Learning

- 사전훈련된네트워크(Pretrained Network)
  - 이미지분류모델 - VGG16 등
- ImageNet
  - 1400만개 레이블된 이미지 + 1000개 클래스 데이터셋

### 사전훈련된네트워크 사용방법

- 특성추출(Feature Extraction) 
  - Pretrained Network 사용하여 특성추출 (일반적 특징)
    - 하위층: 일반적 특성 맵 추출
    - 상위층: 추상적개념(고양이귀 등) 추출
  - Classifier만 새로 훈련 (특정 클래스 정보)
    1. Pretrained Network의 출력을 numpy배열로 저장 > Fully-Connected Classifier에 직접 입력
    2. Pretrained Network 위에 Dense Layer 확장 > PN에 CF추가해서 새 모델 만들어서 학습
       - Conv_base동결 필수 - conv_base.trainable = False
       - 동결 후 compile
       - 훨씬 느림, 연산비용이 매우 커 CPU로는 적용 어려움 > GPU 사용
- 미세조정(Fine Tuning)
  - Conv_base 상위층 몇개를 동결 해제 + Fully-Connected Classifier 추가
  - 상위층: 특화된 특성 학습
  - 훈련할 파라미터가 많아지면 Overfitting 위험 커짐

---



## Convnet Visualization★보충하기

###  convnet filters 시각화

- 필터가 반응하는 시각적 패턴 그리기
- 필터 응답 최대화를 위해 경사상승법(SGA) 적용

### heat maps of class activation 시각화

- 이미지의 어느부분이 Convnet의 최종분류 결정에 기여하는지 확인
- 이미지에 특정물체가 있는 위치 파악에도 사용 가능
- 클래스 활성화 맵(Class Activation Map, CAM) 시각화

---



## RNN(Recurrent Neural Network)

- 텍스트, 시계열, 시퀀스 데이터 처리에 적합
- 기초적인 자연어 이해(Natural Language Understanding)
- 문자언어의 통계적 구조만들어 문제 해결
- 텍스트 벡터화(Vectorizing Text)

### 텍스트 벡터화(Vectorizing Text)

- 단어를 하나의 벡터로 변환
- 문자를 하나의 벡터로 변환
- 단어나 문자의 n-gram을 하나의 벡터로 변환

### 주요용어

- 토큰(Token) - 텍스트 나누는 단위
- 토큰화(Tokenization) - 텍스트를 토큰으로 나누는 작업
- 텍스트 벡터화 - 토큰에 수치형 벡터 연결
  - One-hot encoding - 0 or 1 로 변경
  - Token Embedding - 토큰 사전을 만듦 (딕셔너리)
- N-gram - 문장에서 추출한 n개(이하)의 연속된 단어 그룹
- Bag-of-Words - 특정 순서가 없는 토큰의 집합 (딥러닝에 안쓰임)

### 벡터화 방법

- One-hot encoding
  - 장점: keras 제공, 특수문자제거, 빈도높은 N개 단어 선택
  - 단점: 고유토큰수가 많아지면 사용 어려움, 많은 메모리 사용
- One-hot hashing
  - 알수없는 y값/ 역방향 계산 안됨/ x의 약간 변경으로 y값이 완전히 달라짐
  - 장점: 고유토큰수가 너무 클때 사용, 큰 길이를 넣어도 정해진 길이로 출력됨, 메모리 절약
  - 단점: 해시충돌 문제가 있음(처리방법 다양함), 차원이 토큰수보다 크면 충돌가능성 감소
- Word Embedding
  - 밀집단어 벡터(word vector) 사용
  - 저차원의 실수형 벡터 (적은차원에 더 많은 정보를 저장)
  - 데이터로부터 학습됨
  - 미리 계산된 단어 임베딩을 로드(pretrained word embedding)
  - 단어사이 의미관계 반영(L2 distance(벡터거리) + 방향)
  - 새작업에는 새임베딩 학습필요(주제마다 가중치가 다름 - 역전파사용, Embedding가중치 학습)

### Word Embedding

- 입력: (samples, sequence_length) 2D 정수 텐서/ 길이가 s_l, 개수가 samples
  - 모든 시퀀스는 같은 길이로 0padding or 자름
- 출력: (samples, sequence_length, embedding_dimensionality) 3D 실수 텐서
  - RNN층이나 1D Conv층에서 처리
- 임베딩 결과
  1. Embedding만 사용
     - 75% 정도의 검증정확도
     - 단어사이의 관계, 문장구조 고려되지 않음
  2. word2vec 사용(pretrained)
     - 구체적 의미가 있는 속성을 잡아냄
  3. GloVe(Global Vectors for Word Representation)
     - 단어의 동시출현 통계를 기록한 행렬 분해
- 임베딩 후 Flatten하여 출력함수로 출력
- 사전훈련된 임베딩보다 함께 임베딩 훈련하는게 좋지만, 샘플수가 적으면 정확도 떨어짐

### Feed-Forward Network

- 시퀀스나 시계열을 처리하기위해 전체시퀀스를 하나의 데이터 포인트로 변환해서 입력

### RNN

- 이전 단어를 기억하면서 단어별/한눈에 들어오는만큼 처리
- 과거정보를 사용하여 구축되며 새 정보를 계속 업데이트
- 첫 타임스텝: 0벡터로 초기화
- RNN은 스텝함수로 특화
- 상태: 2개의 다른 시퀀스를 처리하는 사이에 재설정
- 네트워크: 데이터 포인트가 한번에 처리되지 않고 시퀀스의 원소를 차례대로 방문
- 입력: (timesteps, input_features) 2D 텐서
- 진행: 텐서가 입력되면 현재상태와 input_feature연결하여 출력, 다음스텝의 상태로 설정
- 출력: (timesteps, output_features) 2D 텐서
  - 전체시퀀스 정보를 담고있으므로 마지막 출력만 있으면 됨

### SimpleRNN(Layer)

- 하나의 시퀀스가 아닌 시퀀스 배치 처리
- 입력: (batch_size, timesteps, input_features) 3D 텐서
- 출력 - return_sequences
  1. True - (batch_size, timesteps, output_features) 3D 텐서(전체시퀀스)
  2. False - (batch_size, output_features) 2D 텐서(마지막출력)
- 중간층들이 전체시퀀스를 출력하도록 설정해야 하고, 마지막 레이어는 마지막출력만
- 긴 시퀀스 사용하는데 적합하지 않음(짧은문장)
- 학습불가문제: 그래디언트 소실문제(Vanishing gradient problem) 
  - 가중치가 점점 줄어들어서 나중엔 영향이 별로 없어짐
  - 해결: LSTM / GRU 층 사용

### LSTM (Long Short-Term Memory)

- SimpleRNN 변종
- 시퀀스 어느지점에서 추출된 정보가 컨베이어벨트로 올라가 필요시점에서 추가됨
- 오래된 시그널이 소실되는것을 방지
- 이동트랙(carry track) - 이동상태(Ct)

### GRU(Gated Recurrent Unit)

- LSTM과 같은 원리로 작동하지만 간결하고 계산비용이 덜듦
- 

- --