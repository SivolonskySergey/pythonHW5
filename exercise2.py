# 2) Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

count_lines = 0
with open("text_to_count.txt") as f_obj:
    for line in f_obj:
        print(f'в строке № {count_lines} - {len(line.split(" "))} слов')
        count_lines+=1
print(count_lines)