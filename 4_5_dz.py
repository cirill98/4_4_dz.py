# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

with open("file44.txt", "r") as file44:
    data1 = file44.read()
if len(data1) > 20:
    a, b, c = int(data1[0]), int(data1[9]), int(data1[18]) 
    print(a, b, c)
elif len(data1) > 8:
    a, b, c = int(data1[0]), int(data1[9]), 0
    print(a, b)
else: 
    a, b, c = int(data1[0]), 0, 0
    print(a)

with open("file442.txt", "r") as file442:
    data2 = file442.read()
if len(data1) > 20:
    a, b, c = int(data1[0]), int(data1[9]), int(data1[18]) 
    print(a, b, c)
elif len(data1) > 8:
    a, b, c = int(data1[0]), int(data1[9]), 0
    print(a, b)
else: 
    a, b, c = int(data1[0]), 0, 0
    print(a)


result = data1 + '+' + data2
with open("file_result.txt", "w") as file_result:
    file_result.write(result)
print(result)