T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    sum_list = []
    for i in range(n- m + 1):
        sum = 0
        for _ in range(m):
            sum = sum + int(numbers[i])
            i += 1
        sum_list.append(sum)
   
    sum_max = max(sum_list)
    sum_min = min(sum_list)
   
    # sum_min = 100000000000
    # sum_max = -100000000000
    
    
    # for s in sum_list:
    #     if sum_min > s:
    #         sum_min = s
    #     elif sum_max < s:
    #         sum_max = s 
    
    
    print(f'#{test_case} {sum_max - sum_min}')