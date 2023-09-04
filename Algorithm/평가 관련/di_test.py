my_dict = {
    '김씨' : 80,
    '이씨' : 70,
    '박씨' : 60
}

#시험 성적의 합은?
#1
print('#1',sum(my_dict.values()))
# 2, 3, 4, 5
sum = 0
for i in my_dict: #참조 : my_dict.values(), my_dict.items()
    sum = sum + my_dict[i]
    print(i, my_dict[i])
    
print('#2', sum)

#6
def getScore2(dictionary):
    sum = 0
    for i in dictionary.values():
        sum = sum + i
    return sum

print('#3',getScore2(my_dict))
        
        
def getScore(my_dict):
    sum = 0
    for i in my_dict:
        sum = sum + my_dict[i]
    return sum

print('#4', getScore(my_dict))

#70점 이상인 사람의 수는?
def num_of_people(dictionary):
    num = 0
    for i in dictionary.values():
        if i >= 70:
            num = num + 1
    return num

print('#5', num_of_people(my_dict))

#70점 이상 점수의 합은?
def sum_of_people(dictionary):
    sum = 0
    for i in dictionary.values():
        if i >= 70:
            sum = sum + i 
    return sum

print('#6',sum_of_people(my_dict))


#70점 이상 점수의 평균은?

def avg_of_people(dictionary):
    sum = 0
    num = 0
    for i in dictionary.values():
        if i >= 70:
            sum = sum + i 
            num = num + 1
    return sum / num

print('#7', avg_of_people(my_dict))

def avg_of_people2(dictionary):
    # sum = sum_of_people(dictionary)
    # num = num_of_people(dictionary)
    # return sum / num
    return sum_of_people(dictionary) / num_of_people(dictionary)
print('#8', avg_of_people2(my_dict))