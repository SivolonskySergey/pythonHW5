# 5) Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def file_w_nums(filename):
    summ_result = 0
    str_nums = input('Введите числа через пробел: ')
    with open("summ.txt", "w") as f_obj:
        print(str_nums, file=f_obj)
    open_f = open('summ.txt')
    content = open_f.readlines()
    to_list = content[0][:-2].split()
    for el in to_list:
        summ_result+=int(el)
    print(summ_result)
file_w_nums('summ.txt')