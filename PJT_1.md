### 서버에 데이터 요청하는 방법
- requests python library 사용
- 브라우저 켜서 url 입력


`get` 데이터 요청 함수
`requests.get(url)` 해당 서버 urll 에 데이터를 달라고 요청을 보내는 함수

### API

- 클라이언트가 원하는 기능을 수행하기 위해서 서버 측에 만들어 놓는 프로그램
  - 기능예시 : 데이터 저장, 조회, 수정, 삭제 등등
- 서버측에 특정 주소로 요청이 오면 정해진 기능을 수행하는 API를 미리 만들어 둠
  - 클라이언트는 서버가 미리 만들언호은 주소로 요청을 보냄
- 정보 수집을 위해
  - 정보를 가지고 있는 서버
  - 해당 서버가 제공하는 API
#### open API
- 사용자 인증 후 API KEY 발급
- 클라이언트는 서버에게 요청과 api key 까지 보냄
- 사용량 제한 확인하기

#### API 가 사용하는 데이터 형식 -JSON
- 자바스크립트 객체 표기법 javascriptobjectnotation
- 데이터를 저장하거나 전송할 때 많이 사용되는 경량의 텍스트 기반의 데이터 형식
- 통신 방법이나 프로그래밍 문법이 아니라 단순히 데이터를 표현하는 표현 방법 중 하나



```python
new_dic = {}  
#참조TYpe은 아이디를 기준으로 관리되기 때문에 주의!!!
new_list =[]
for i in range(5):    
    new_dic['key'] = i
    new_list.append(new_dic)
print(new_list)
#[{'key': 4}, {'key': 4}, {'key': 4}, {'key': 4}, {'key': 4}]
```

```python
new_list =[]
for i in range(5):
    new_dic = {}
    new_dic['key'] = i
    new_list.append(new_dic)
print(new_list)
#[{'key': 0}, {'key': 1}, {'key': 2}, {'key': 3}, {'key': 4}]
```

```python
new_list =[]
for i in range(5):
    new_dic = {'키' : i}
    new_list.append(new_dic)
print(new_list)
```