# Задача "Нули ничто, отрицание недопустимо!":
# Дан список чисел [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# Нужно выписывать из этого списка только положительные числа до тех пор,
# пока не встретите отрицательное или не закончится список (выход за границу).
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
count = 0
while count < len(my_list):
    num = my_list[count]
    count = count + 1
    if num == 0:
        continue
    elif num < 0:
        break
    else:
        print(num)