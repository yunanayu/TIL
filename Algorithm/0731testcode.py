# problem 11

def get_maxsum(matrix):
    cnt_col = 0
    for c in matrix[0]:
        cnt_col += 1
    
    cnt_row = 0
    for r in matrix:
        cnt_row += 1

    cur_max = 0
# 가로합
    for r in range(cnt_row):
        total = 0
        #for c in matrix[r]:
        for c in range(cnt_col):
            total += c
        if cur_max < total:
            cur_max = total
# 세로합
    for c in range(cnt_col):
        total = 0
        for r in range(cnt_row): #matrix[r][0]:
            total = matrix[r][c]
        if cur_max < total :
            cur_max = total
    return cur_max            
    
#chr(ord('A') + ('A'로부터 몇칸? + num) % 26)   #ord('C')- ord('A')
############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum, min, max, len 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def caesar(word, num):
    pass
    # # 여기에 코드를 작성하여 함수를 완성합니다.
    result = '' #결과값 저장
    for i in word: # word의 문자마다 반복
        if i.islower(): #문자가 소문자일때
            if ord(i) + num > 122: #변환값이 122 가 넘는다면
                result = result + chr(ord(i) + num - 26) #변환값에서 26을 빼 준 후 num 를 더하여 알파벳으로 재변환
            else:   # 변환값이 122를 넘지 않으면 num 만큼 더해서 문자로 재변환
                result = result + chr(ord(i) + num)
        elif i.isupper():  #문자가 대문자일때 소문자와 같은 방식으로 작동
            if ord(i) + num > 90:
                result = result + chr(ord(i) + num - 26)
            else:
                result = result + chr(ord(i) + num)
    return result


# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    print(caesar('ssafy', 1))   # => ttbgz
    print(caesar('Python', 10)) # => Zidryx
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    
