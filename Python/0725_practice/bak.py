# A, B, C = map(int, input().split())
# print((A + B) % C)
# print(((A % C) + (B % C)) % C)
# print((A * B) % C)
# print(((A % C) * (B % C)) % C)

# num = int(input())
# number = input()
# num_list = []
# for i in number:
#     num_list.append(i)


# c = num * int(num_list[2])
# d = num * int(num_list[1]) 
# e = num * int(num_list[0])
# f = c + d*10 + e*100
# print(c)
# print(d)
# print(e)
# print(f)

# a, b, c = map(int,input().split())
# print(a + b + c)

# print('|\_/|')
# print('|q p|   /}')
# print('( 0 )"""\\')
# print('|"^"`    |')
# print('||_/=\\\__|')

#1330
# a, b = map(int,input().split())
# if a > b:
#     print('>')
# elif a < b:
#     print('<')
# else:
#     print('==')

#9498
# a =int(input())

# if 90 <= a <=100:
#     print('A')
# elif 80<= a <=89:
#     print('B')
# elif 70<= a <= 79:
#     print('C')
# elif 60<= a <= 69:
#     print('D')
# else:
#     print('F')

#2753
y = int(input())

if y % 400 == 0:
    print('1')
elif y % 4 == 0 and y % 100 != 0:
    print('1')
else:
    print('0') 