# value = 5
# cnt = 3

# 재귀함수

def mul(value, cnt):
    if cnt == 1:
        return 5
    return value * mul(value, cnt-1)


# 5까지 다 더하는 재귀 함수
def rec(num):
    if num == 1:
        return 1
    return rec(num -1) + num

print(mul(5, 3))

print(rec(5))

#팩토리얼 함수

def fac(n):
    if n == 1:
        return 1
    return fac(n-1) * n

#리스트의 합을 구하는 재귀함수

lst = [2, 3, 6, 9, 10]

def sum_list(n):
    if n == 0 :
        return lst[0]
    return sum_list(n-1) + lst[n]
    
    
print(sum_list(4)) #마지막 인덱스 값

#

def sum_lst(n, cur_sum):
    return sum_lst(n+1, cur_sum+lst[n+1])
    
    
print(sum_lst(0, lst[0])) #마지막 인덱스 값
