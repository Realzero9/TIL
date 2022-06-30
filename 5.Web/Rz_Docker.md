# Docker

## 1. Image Build (이미지 빌드)

```bash
$ docker build -t [IMAGE NAME]:[tag] .
```

- OPTION
  - `-t` : build할 Image에 대한 tag 설정
  - `.` : 현재 폴더내용 전부

## 1-1. Image 확인

```bash
$ docker images
```

* 예시
  `REPOSITORY   TAG       		IMAGE ID       CREATED          SIZE
  [IMAGE NAME]  latest[tag]    	52869f7f042e   1 minutes ago   	4.49GB`

* 지금 (로컬에서) 생성되어 있는 도커이미지 리스트를 확인 할 수 있음

## 2. docker run(도커이미지 운영)

```bash
$ docker run -d -p [HostPort]:[UserPort] [IMAGE NAME]:[tag]
```

* `http://localhost:[HostPort]` 로 연결 가능
* (로컬에서) 가지고 있는 이미지를 운영할 수 있음

## 2-1. Docker Container Running 확인 (도커컨테이너 확인)

```bash
$ docker ps
```

* 예시
  `CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES`
* 현재 운영중인 컨테이너 리스트를 확인할 수 있음

# Docker Run (Image 원격서버에서)

## 1. 이미지 파일 저장

```Linux
$ docker save [IMAGE NAME] > [FileName].tar
```

## 2. tar 파일 원격서버에 전송

```Linux
$ scp [FileName].tar [User]@[ServerIP]:[FilePath.FileName].tar
```

## 3.  [SSH 접속](#SSH) 해서  tar파일을 image로 저장

```Linux.server
$ sudo docker load < [FileName].tar
```

## 4. image 실행

```Linux.server
$ sudo docker run --name [ContainerID] -p [HostPort(8000)]:[ContainerPort(8000)] [IMAGE NAME]:[tag]
```

# SSH

## 1. ssh key 생성 (~)

```bash
$ ssh-keygen
```

* id_rsa 및 id_rsa.pub 파일이 만들어짐
* 경로를 자동으로 지정해주며, password를 입력할 수 있음(생략가능)
* `key fingerprint` 생성되며 `key's randomart image` 출력

## 2. id_rsa 확인

```bash
$ cd .ssh
$ ls
```

## 3. authorized_keys, config 파일 생성

```bash
$ vi authorized_keys
```

* id_rsa.pub 내용 복붙해서(esc+i = 수정) 저장 (esc + :wq = 저장)

```bash
$ vi config
```

* `Host [HOST NAME]
          HostName [HOST IP]
          Port 22
          User [User NAME]`
  위와 같이 작성 후 (esc+i = 수정) 저장 (esc + :wq = 저장)

## 4. ssh login

```bash
$ ssh [HOST NAME]
```

* password 입력하면 ssh 접속 완료

