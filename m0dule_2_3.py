# Стиль кода часть II. Цикл While.
# ============================================
# import this
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
print(my_list)
print(len(my_list))
i = 0
while i < len(my_list):
    if my_list[i] > 0:
        print(my_list[i])
        i = i + 1
        continue
    if my_list[i] < 0:
        break
    print(my_list[i])
    i = i + 1

