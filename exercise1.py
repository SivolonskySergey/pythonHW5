# 1) Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

file_name = (f'{input("Введите имя файла: ")}.txt')

def add_text(name, mode = 'a'):
    user_str = None
    while user_str != '':
        user_str = input("Введите текст: ")
        with open(name, mode) as f_obj:
            print(f'{user_str} \n', file=f_obj)

add_text(file_name, "a")
