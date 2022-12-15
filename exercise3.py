# 3) Создать текстовый файл (не программно), построчно записать фамилии
# сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

summ_salary = 0
workers_counter = 0
with open('salary.txt') as content:
  for line in content:
    workers_counter+=1
    worker = line.split()
    curr_salary = float(worker[1])
    summ_salary+=curr_salary
    if curr_salary < 20000:
      print(worker[0])


print(f'Средняя з/п по сотрудникам - {round(summ_salary / workers_counter, 2)}')