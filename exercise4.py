# 4) Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и
# считывающую построчно данные. При этом английские числительные должны
# заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

def open_n_add(filename, mode, content_f):
  open_f = open(filename, mode)
  open_f.write(f'{content_f} \n')
  open_f.close()

with open('new_text.txt') as new_text:
  file_open = open('rus_file.txt', 'w')
  file_open.write('')
  file_open.close()
  for line in new_text:
    curr_line = line.split()
    if curr_line[0] == 'One':
      curr_line.pop(0)
      curr_line.insert(0, 'Один')
      to_str = ' '.join(curr_line)
      open_n_add('rus_file.txt', 'a', to_str)
      print(to_str)
    elif curr_line[0] == 'Two':
      curr_line.pop(0)
      curr_line.insert(0, 'Два')
      to_str = ' '.join(curr_line)
      open_n_add('rus_file.txt', 'a', to_str)
      print(to_str)
    elif curr_line[0] == 'Three':
      curr_line.pop(0)
      curr_line.insert(0, 'Три')
      to_str = ' '.join(curr_line)
      open_n_add('rus_file.txt', 'a', to_str)
      print(to_str)
    elif curr_line[0] == 'Four':
      curr_line.pop(0)
      curr_line.insert(0, 'Четыре')
      to_str = ' '.join(curr_line)
      open_n_add('rus_file.txt', 'a', to_str)
      print(to_str)
