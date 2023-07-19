def greeting(name,age):
    print(f'안녕, {name}, {age}!!!')

greeting('Alicce', 25) #안녕, Alicce, 25!!!

greeting(25, 'alice') #안녕, 25, alice!!!

greeting(age=25, name='alice') #(키워드 인자) 안녕, alice, 25!!!

num = 100

def my_func():
    print(num)

my_func()   #바깥 변수에 접근 가ㄴ,ㅇ
#좋은 코드 아니니 이렇게 코드작성 금지


print(sum([1, 2, 3]))  #6

sum = 10

print(sum([1, 2, 3]))
#TypeError: 'int' object is not callable

#sum 을 참조 시 LEGB 룰에 따라 global 에서 먼저 찾기 때문에 built in scope 에 있던
#내장함수 sum을 작성하지 못하게 됨.