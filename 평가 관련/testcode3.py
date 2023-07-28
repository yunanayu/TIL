#

def make(chr, n):
    if n == 0:
        return chr
    return make(chr, n-1) + chr
make('a', 5) # a a a a a 

def make2(cnt):
    if cnt == 0:
        return lst[0]
    # return make2(cnt-1) + lst[cnt]
    # return lst[cnt] + make2(cnt-1)

lst = ['h', 'e', 'l', 'l', 'o']
cnt = 0
for c in lst:
    cnt += 1
print(make2(cnt-1))

# a = 123
# print(list(map(int,str(input()))))

# num = list(map(int,str(input())))
# print(sum(num))