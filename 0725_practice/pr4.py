#슬라이싱(얕은복사)

#얕은 복사의 한계
# a = [1, 2, [1, 2]]

# b = a[a::]
# b[2][0] = 999
# print(a, b)

#깊은 복사
import copy
original_list = [1, 2, [1, 2]]
deep_copied_list = copy.deepcopy(original_list)

deep_copied_list[2][0] = 999

print(original_list, deep_copied_list)