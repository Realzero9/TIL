# PaaS(Platform as a service)

- 클라우드 컴퓨팅 서비스형 플랫폼
- 앱 개발 및 구현시 관련 인프라 만들고 유지보수하는 복잡함 없이 앱을 개발, 실행, 관리할 수 있는 플랫폼 제공
- 클라우드에서 제공되는 완전한 개발 및 배포환경
- 서버, 저장소, 네트워킹, 미들웨어, 개발도구, BI, 서비스, 빌드, 테스트, 배포, 관리, 업데이트 등

## [NAVER CLOUD](#navercloud)

- [Container Registry](https://guide.ncloud-docs.com/docs/container-ncr-1-1)
  - 도커컨테이너 이미지 저장소
  - 컨테이너 이미지 저장, 관리 및 배포 도와줌
  - 컨테이너레지스트리 서비스 자체는 무료, 추가로 기능 사용한 부분에 대한 (Object Storage) 사용량의 비용 발생

---

## [AWS/Azure/GCP장단점](https://moondol-ai.tistory.com/184)

- 요즘 추세는 멀티클라우드방식 대세(각 클라우드 제공사의 장점만 뽑아서 활용)

## AWS

- 다양하고 탄탄한서비스

## MS Azure

- 오픈소스 및 통합

## GCP(Google Cloud Platform)

- 데이터 분석 및 AI 기술

---

## 오라클

- [오라클PaaS](https://www.oracle.com/kr/cloud/what-is-paas/)
- [오라클장단점](https://hi098123.tistory.com/404)
- 30일 무료
- JAVA 기반
- 비용은 월300달러 정도

## 헤로쿠(Heroku)

- Github에 연결가능
- [헤로쿠배포참고1](https://nhj12311.tistory.com/276)

## Netlify

- 클라우드 컴퓨팅
- 웹 애플리케이션 및 정적 웹사이트를 위한 호스팅 및 서버리스 백엔드 서비스를 제공

## Github Pages

- 1계정당 1page만 제공됨(?)

- 정적웹페이지 배포

- Github Repository에 연결하면 사용가능

- 프로젝트에 깃허브페이지 설치해야 한다고 함

  ```python
  npm install gh-pages --save-dev
  ```

- [깃페이지배포참고1](https://velog.io/@byjihye/react-github-pages)

- [깃페이지배포참고2](https://velog.io/@bigyou98/GitHub-Page-%EB%B0%B0%ED%8F%AC%ED%95%98%EA%B8%B0)

## GoormIde

- [구름장단점](https://m.blog.naver.com/topblade71/221501135961)
- 리눅스 기반

# 소프트웨어 플랫폼

- [웹프레임워크](https://ko.wikipedia.org/wiki/%EC%9B%B9_%ED%94%84%EB%A0%88%EC%9E%84%EC%9B%8C%ED%81%AC)

## FASTapi

- 비동기 방식이 가능한 python web server framework
- [FASTapi 장단점](https://velog.io/@maintain0404/Django%EA%B0%9C%EB%B0%9C%EC%9E%90%EC%9D%98-FastAPI-%EC%82%AC%EC%9A%A9-%ED%9B%84%EA%B8%B0)
- 특징
  1. 데이터타입을 엔드포인트(특정서비스의 클라이언트들이 접근할 수 있는 웹주소URL)로 명시하지 않아도 된다(알아서 바꿔줌)
  2. Uvicorn ASGI Server 사용
     - ASGI : Asynchronous Server Gateway Interface
       	비동기 웹서버(DB, API연동과정중 대기시간 낭비없이 다른작업도 하는 방식)
- 장점
  1. 빠르다
  2. 코드간단
  3. 적은버그

### Uvicorn

- 비동기방식의 http server  = ASCI

## Node.js

- 이것도 네이버클라우드에서 제공중...(추가로알아봐야함)

## Django 

- [장고위키](https://ko.wikipedia.org/wiki/%EC%9E%A5%EA%B3%A0_(%EC%9B%B9_%ED%94%84%EB%A0%88%EC%9E%84%EC%9B%8C%ED%81%AC))

## Flask 

- [플라스크위키](https://ko.wikipedia.org/wiki/%EC%9B%B9_%ED%94%84%EB%A0%88%EC%9E%84%EC%9B%8C%ED%81%AC)

# 로컬 접근- 외부인터넷

## 포트포워딩(공유기)

- 로컬을 외부 인터넷 망에서 http 또는 https로 접속하는 방법

## ngrok

- 외부 인터넷망에서 로컬로 접속하는 방법
- 임시 도메인 할당, 웹훅(Webhook) 테스트시 유용(유료)
  - 웹훅 : endpoint에서 이벤트 발생하면 app으로 수신되는 형태(Reverse API, Web Callback, HTTP PUSH API), 알림봇 <-> polling
  - 계정가입x : 세션 8시간 유지가능
  - 계정가입o : Auth Token발급으로 세션만료 제한없음
  - 무료 : 도메인네임 랜덤, ngrok 재실행시 변경됨
- NAT 및 방화벽 뒤에 있는 로컬 서버를 보안터널을 통해 공용 인터넷에 접속하는 방법을 제공
- 웹인터페이스 지원

# navercloud

## [소규모 웹사이트 인프라 구성](https://youtu.be/TdLU504n3GA)

1. [DNS](https://ko.wikipedia.org/wiki/%EB%8F%84%EB%A9%94%EC%9D%B8_%EB%84%A4%EC%9E%84_%EC%8B%9C%EC%8A%A4%ED%85%9C)(Domain Name System) : 도메인 네임 시스템
   호스트의 도메인 이름을 호스트의 네트워크 주소로 바꾸거나 그 반대의 변환을 수행

   - [LoadBalancer](https://nesoy.github.io/articles/2018-06/Load-Balancer) : 트래픽이 많을 때 여러 대의 서버가 분산처리하여 해결

     - NAT(Network Address Translation) : 공유기 개념
       사설 IP 주소를 공인 IP 주소로 바꾸는데 사용하는 통신망의 주소 변조기

     - Tunneling
       인터넷 상에 보이지 않는 통로를 만들어 통신할 수 있게 함
       데이터를 캡슐화 해서 연결된 상호 간에만 캡슐화된 패킷을 구별해 캡슐화 해제

     - DSR(Dynamic Source Routing protocol)
       서버에서 클라이언트로 돌아가는 경우 목적지 주소를 스위치의 IP주소가 아닌 클라이언트의 IP 주소로 전달해서 네트워크 스위치를 거치지 않고 바로 클라이언트를 찾아가는 개념

       ```markdown
       Client -> (Switch) ->  **Server -> Client**
       ```

2. [Webserver](https://ko.wikipedia.org/wiki/%EC%9B%B9_%EC%84%9C%EB%B2%84) : 웹 브라우저와 같은 클라이언트로부터 HTTP 요청을 받아들이고, HTML 문서와 같은 웹페이지를 반환하는 컴퓨터 프로그램

3. Cloud DB : 클라우드 환경, 프라이빗, 퍼블릭 또는 하이브리드 클라우드에서 구축, 배포 및 액세스 되는 데이터 베이스

---

# 도메인 연결

1. 도메인 준비
   - 도메인 발급
     - ex) freenom.com
   - 공인 IP
2. NaverCloud
   - 네이버DNS 서버 발급
   - (구입한) 도메인과 연결