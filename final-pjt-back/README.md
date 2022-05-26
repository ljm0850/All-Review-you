```
완료
accounts
api/v1/accounts/login/				//[POST] 로그인 요청
requests ; username, password
responses ; token

api/v1/accounts/signup/				//[POST] 회원가입 요청
requests ; username, password, email, first_name, last_name
responses ; token 

api/v1/accounts/logout/				//[POST]: 로그아웃 요청
requests ; token
responses ; status

api/v1/accounts/password/change/				//[POST]: 비밀번호 변경
[POST]
requests ; new_password1, new_password_2, old_password
responses ; status

api/v1/accounts/user/				//[GET]: 회원정보 요청 [PATCH] 업데이트 요청
[GET]
requests ; token,
responses ; username, first_name, last_name
[POST]
requests ; token, password, email,
responses ; status


api/v1/accounts/profile/ 		// [GET] user-data, review list 요청
requests ; token,
responses ; user-data, reviews


api/v1/accounts/<username>/follow/ - 팔로우	//[PUT]: 팔로우 요청 
requests ; Token
responses ; status
```

