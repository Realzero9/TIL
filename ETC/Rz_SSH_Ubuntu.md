# SSH - id/password 설정 (Ubuntu)

```bash
> ssh-keygen
# 경로지정 + password 설정 (none)
The key fingerprint is:
SHA256:******************************************* **@***
The key's randomart image is:
+---[RSA ****]----+
|  ***            |
|  ** *           |
| * ****  *       |
|* * *****        |
| ********        |
|********         |
|********         |
|**** ***         |
| ********        |
+----[SHA256]-----+

> cd .ssh

> ls
id_rsa  id_rsa.pub
```

# authorized_keys, config  vi로 파일 생성

```bash
> vi authorized_keys
id_rsa.pub
# 내용 복붙
# (esc+i = 수정) 저장
# (esc + :wq) 빠져나오기
> vi config
'''Host [HOST_ID]
		'''HostName [ServerUrl]
		 '''Port 8000
		 '''User [UserName]
# (esc+i = 수정) 저장
# (esc + :wq) 빠져나오기
```

# SSH로그인

- 네이버서버로 접속

```bash
> ssh [HOST_ID]
password: # (네이버서버에서 관리자 비밀번호 얻어서 입력)
```