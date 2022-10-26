# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


with open('file.txt', 'r') as file:
    text = file.readline()
    txt_compr = text.split()

print(text)

def f_cod(txt):
    coding = ''
    prev_char = ''
    count = 1
    if not txt:
        return ''

    for char in txt:
        if char != prev_char:
            if prev_char:
                coding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        coding += str(count) + prev_char
        return coding


txt_compr = f_cod(text)

with open('file_coding.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{txt_compr}')
print(txt_compr)