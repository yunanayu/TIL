# len, sum , min, max 함수
def my_len(lst):
    # res = len(lst)
    res = 0
    for i in lst:
        res += 1
    return res

def my_sum(lst):
    # res = sum(lst)
    res = 0
    for i in lst:
        res += i
    return res

def my_min(lst):
    # res = min(lst)
    # idx = lst.index(min(lst))
    # list(enumerate(lst))
    cur_min = 1e10
    # = cur_min = lst[0]
    cur_min_idx = -1
    for idx, value in enumerate(lst):
        if cur_min > value:   #>= 을 하게 되면 같은값까지 비교, > 인 경우 같은값의 인덱스 값은 넘어감
             cur_min = value
             cur_min_idx = idx
         
    return cur_min, cur_min_idx

def my_max(lst):
    # res = max(lst)
    # idx = lst.index(max(lst))
    cur_max = 1e10
    # = cur_min = lst[0]
    cur_max_idx = 0
    for idx, value in enumerate(lst):
    #= for idx in range(my_len(lst)):    
        if cur_max < value:
             cur_max = value
             cur_max_idx = idx
         
    return cur_min, cur_max_idx
    return res, idx

numbers = [10, 2, 5, 7, 12]
print(my_len(numbers))



#max,min 구하는 법
cur_max = -1
cur_min = 10001
cur_sum =0
for n in numbers:
    if n > cur_max:
            cur_max = n
    if n < cur_min:
            cur_min = n
    cur_sum += n
print(cur_sum,cur_max,cur_min)






def get_len(numbers): #짝수 개수 구하기
    
    l = 0
    
    for n in numbers:
        if n % 2 == 0:
            l += 1
    return 1

numbers = [2, 5, 7, 10, 6]
get_len(numbers)
    
#chr, ord 활용
#문자와 숫자 사이의 변경
print(chr(ord('A') + 2))  #ord -> 문자를 문자번호로 chr -> 문자번호를 숫자로/// 대소문자 코드 다름

#이차원 배열
a = [
    [1, 2, 3],
    [3, 4, 5],
    [2, 5, 6],
    [12, 5, 6]
]
a0 = a[0]
print(a0[1])
print('----------------------------')

cur_max = 0
for r in range(4):
    s = 0
    for c in range(3):
        # print(a[r][c])
        s = s + a[r][c]
    print('sum=', s)   
    if cur_max < s :
        cur_max = s

print('----------------------------')
       
for i in range(3):
    print(a[0][i])

print('----------------------------')
    
for c in range(3):
    print(a[1][c])

print('----------------------------')

for c in range(3):
    print(a[1][c])
    
print('----------------------------')


# 4가 있는 위ㅊㅣ는?

def getFour(numbers):
    for r in range(row):
        for c in range(col):
            #print(numbers[r][c])
            if numbers[r][c] ==4 :
                return r, c

a = [
    [1, 2, 3],
    [3, 4, 5],
    [2, 5, 6],
    [12, 5, 6]
]

row = 4
col = 3    
print(getFour(a))
#찾는 데이터가 양 끝에 있을때도 잘 나오는지 확인하기.


# 열의 합 구하기
a = [
    [1, 2, 3],
    [3, 4, 5],
    [2, 5, 6],
    [12, 5, 6]
]

for c in range(col):
    for r in range(row):
        print(a[r][c])
        
        
#--------- 자리 이동???
row = 4
col = 3
cur_row , cul_col = getFour(a)
for i in range(2):
    cul_col += 1
    if cul_col > 2 :#더이상 갈 수 없으면
        break
    
    
# 입력값 받기
i = input() #3 4 5
i = i.split() ['3', '4', '5']
i = list(map(int, input().split())) #[3, 4, 5]

print(i, type(i))

r = []
for _ in range(4):
    i = list(map(int, input().split()))
    r.append(i)
print(r)
# 위 아래 r 같은 결과 나옴
r = [list(map(int, input().split())) for _ in range(4)]

s = [1, 1, 1]
s = [1] * 3
print(s) # [1, 1, 1]

s = [[1] * 3] * 4
print(s) #[[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]] 
# 아이디를 복사해오는거라 s[0][1] =100 으로 값을 바꾸면 4개 모두 [1, 100, 1]로 바뀜

s = [[1] * 3 for _ in range(4)]
print(s)
s[0][1] = 100
print(s) #[[1, 100, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]] 