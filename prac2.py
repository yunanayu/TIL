numbers = [1, 2, 3]
result = map(str, numbers)

print(result) #<map object at 0x0000020AA9AC6E20>
print(list(result)) #['1', '2', '3']

result = []
for number in numbers:
    result.append(str(number))

print(result)  #map 기능 수행하는 코드


def my_func(x):
    result = x * 2
    return result

print(list(map(my_func, numbers)))

names = ['A', 'B', 'C']
ages = [30, 25, 35]
cities = ['N', 'L', "p"]

for name, age, city in zip(names, ages, cities):
    print(f'{name} is {age}years old and lives in {city}')

# map + lambda  이름 없이 함수 사용 일회성쓸때 사용
numbers = [1,2,3,4,5]
result = list(map(lambda x: x * 2, numbers))
print(result)

#재귀함수

def factorial(n):  # n = 5 # n -> 지역변수 역할
    if n == 1:
        return 1
    
    t = n * factorial(n-1)  #함수가 factorial을 다시 호출
    return t
print(factorial(5))  #가장 먼저 실행됨

#정의는 이름 하나당 한번만 만듦. 호출은 계속 쌓임


def my_print(s):
    s = s + '!!!'
    print(s)

s = 'abc'
my_print(s)  #abc!!!
s = my_print(s)  #assignment  연산자 가장 마ㅈ막
print(s)  #none

s= [1, 2, 3]



def aaa(n):
    if n >10:
        return 'zmek'

print(aaa(3)) #None  해당하는 값이 반환되지 않기 때문에 None  cnffur


def my_print(lst_s):
    lst.append(10)
    #t = lst[::]
    t.append(10)
    print(lst)
    return

s = ['a','b']
my_print(s)
print(s)

#--------------
res = 0
def double_a(a):
    t = a*2
    return t

var_a = 10
res = double_a(var_a)
print(res)

#--------------------
#3.2
def create_user(name, age, address):
    #user_info = {'name':name, 'age':age, 'address':address}
    #print(user_info)
    user_info = {}
    user_info['name'] = name
    user_info['age'] = age
    user_info['address'] = address

    #print(user_info)

    return 
user_info = create_user('홍길동', 20, '광주')
print(user_info)