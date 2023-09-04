# lst = [3, 14, 5, 6, 7, 8, 10, 1]
# N = len(lst)

# 일차원 배열과 반복문 연습

# sumV = 0
# for d in lst:
#     sumV += d

# sumV = 0
# for i in range(N):
#     sumV += lst[i]
    
# maxV = 0
# for x in range(len(lst)):
#     if maxV < lst[x]:
#         maxV = lst[x]
# print(maxV)

# minV = lst[0]
# for n in range(len(lst)):
#     if minV > lst[n]:
#         minV = lst[n]
# print(minV)

# 간격을 입력 받아 (0, i-1)을 시작으로 하는 합을 구해 최소값

# minV = 100*N-1
# K = 3 # 간격

# sumV = 0
# for i in range(0, N, 3):
#     sumV += lst[i]
# print(sumV)

# for s in range(3):  # 시작점 설정
#     sumV = 0
#     for i in range(s, N, 3):
#         sumV += lst[i]
#     print(sumV)

# for s in range(K):  # 시작점 설정
#     sumV = 0
#     for i in range(s, N, K): # 시작점, 끝점, 간격 입력
#         sumV += lst[i]
#     print(sumV)
#     if minV > sumV:     # 최소값 구하는 코드
#         minV = sumV
# print(minV)



# for k in range(2, 5): # 간격값이 주어지는것이 아니라 2-4까지의 간격 문제로 확장 될 때 사용
#     for s in range(k):  # 시작점 설정
#         sumV = 0
#         for i in range(s, N, K): # 시작점, 끝점, 간격 입력
#             sumV += lst[i]
#         print(sumV)
#         if minV > sumV:
#             minV = sumV
#     print(minV)
# ---------------------------------------------------------------------------------------------------

# 구간 합 구하기 : 구간합을 구해서 최대와 최소의 차이를 출력해라

# N = 8
# lst = [3, 14, 5, 6, 7, 8, 10, 1]
# M = 5 

# for s in range(N-M+1): # 스타트 지점
#     sumV = 0
#     for i in range(s, s+M):
#         sumV += lst[i]

#     #print(sumV)

# ------------------------------------------------------------------------

# 이차원 배열과 반복문 연습

# N = 5   # 행의 수
# M = 4   # 열의 수
# arr = [[1, 2, 3, 4], [4, 3, 2, 1], [4, 5, 6, 7], [4, 5, 6, 7], [4, 5, 6, 7]]
# # arr = [list(map(int, input().split())) for _ in range N]

# # 전체 합
# total = 0 
# for r in range(N):
#     for c in range(M):
#         total += arr[r][c]
# print(total)

# # 행별 합
# for r in range(N):
#     total = 0
#     for c in range(M):
#         total += arr[r][c]
#     print(total)

# 최대 최소 구하기


# 부분 위치의 합 구하기

# N = 5   # 행의 수
# M = 4   # 열의 수
# arr = [[1, 2, 3, 4], [4, 3, 2, 1], [4, 5, 6, 7], [4, 5, 6, 7], [4, 5, 6, 7]]

# 첫번째 방법

# start_row , start_col = 1, 0
# sizeR = 2 
# sizeC = 3  #의 합을 구하기 
# # # -> [4, 3, 2, 1] + [4, 5, 6, 7]

# sumV = 0
# for r in range(start_row, start_row+sizeR):
#     for c in range(start_col, start_col+sizeC):
#         if 0 <= r < N and 0 <= c < M: # 좌표가 영역 안에 있을 때 만 더하기 # 항상 행 열 개수 주의!!
#             sumV += arr[r][c]

# 두번째 방법

# s = (1, 0)
# e = (4, 2)  # 스타트 지점

# sumV = 0
# for r in range(s[0], e[0]+1): # 포함인지 포함이 아닌지 꼭 확인하기
#     for c in range(s[1], e[1]+1):
#         sumV += arr[r][c]


# --------------------------------------------------------

# # 첫번째 행의 합
# maxV = 0
# result = 0
# sumV = 0
# for c in range(M):
#     sumV += arr[0][c]

# if maxV < sumV:
#     maxV = sumV
#     result = 0

# # 마지막 행의 합

# sumV =0
# for c in range(M):
#     sumV += arr[N-1][c]
# if maxV < sumV:
#     maxV = sumV
#     result = 1
    

# sumV =0
# for r in range(N):
#     sumV += arr[r][0]
# if maxV < sumV:
#     maxV = sumV
#     result = 2
    


# sumV =0
# for r in range(N):
#     sumV += arr[r][N-1]
# if maxV < sumV:
#     maxV = sumV
#     result = 3

#--------------------------------------------------------
# 이차원 배열과 반복문 연습
N = 5   # 행의 수
M = 4   # 열의 수
arr1 = [[1, 2, 3, 4], [4, 3, 2, 1], [4, 5, 6, 7], [4, 5, 6, 7], [4, 5, 6, 7]]
arr2 = [[1, 2, 3, 4], [1, 2, 2, 1], [7, 6, 6, 7], [4, 5, 6, 7], [4, 5, 6, 7]]

# 조건 범위만큼 더한 후 새로운 행렬 만들어서 출력하기
# arr1 시작 위치 (sr1, sc1)
# arr2 시작 위치 (sr2, sc2)
# 크기 SN = 2 , SM = 3

s_1 = (1, 1)
s_2 = (2, 0)

SN = 2 
SM = 3

sum_arr = [[0] * SM for _ in range(SN)]

for r in range(SN):
    for c in range(SM):
        sum_arr[r][c] = arr1[s_1[0]+r][s_1[1]+c] + arr2[s_2[0]+r][s_2[1]+c]
print(sum_arr)
