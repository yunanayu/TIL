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
