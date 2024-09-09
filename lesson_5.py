print('lesson_5')   # задание №5. Списки. Кортежи

# создаём кортеж
my_tuple = (333, 3.14, 'I am a program', False, ['one', 'two', 'three'], (1, 2, 3))

# печатаем ифромацию о кортеже
print('Я программа, у меня есть переменная my_tuple, она относится к', type(my_tuple), 'и содержит в себе', len(my_tuple), 'элемент(а,ов)')

# печатаем элементы кортежа
print('Вот эти элементы:', my_tuple)

# печатаем тип элементов кортежа
print('Эти элементы относятся к следующим классам: ')
for element in my_tuple:
    print(type(element))

# пробуем изменить элемент списка
# my_tuple[3] = True

# пришлось закомментировать команду, она вызывает ошибку.

# Элементы кортежа нельзя изменить. Кортеж относится к неизменяемым данным.
# Исключение, если только элемент кортежа относится к изменяемым данным.
# например мы можем поменять элемент в списке, который сам является элементом кортежа

my_tuple[4][0] = 'four'
print('Мне кажется, внутри элемента кортежа что-то поменялось... Давайте посмотрим:',my_tuple)

# создаём список
my_list = [True, (11, 12, 13), ['eleven', 'twelve', 'thirteen'], 'You are a human', 100, 2.71828]

# печатаем ифромацию о списке
print('Также у меня есть переменная my_list, она относится к', type(my_list), 'и содержит в себе', len(my_list), 'элемент(а,ов)')

# печатаем элементы списка
print('Вот эти элементы:', my_list)

# печатаем тип элементов списка
print('Эти элементы относятся к следующим классам: ')
for element in my_list:
    print(type(element))

# меняем первый элемент списка
my_list[0] = False

# печатаем изменённый список
print('Ой, у списка заменили один элемент! Посмотрите, что получилось:',my_list)

'''
# список
weapons = ['gun','rifle','pistol']
print(weapons)
print(weapons[1])
weapons[0] = 'laser'
print(weapons)
weapons[2] = 'plazma'
print(weapons)
weapons.append(True)
print(weapons)
weapons.extend("canon")
print(weapons)
weapons.extend(["rocket", 3])
print(weapons)
weapons.remove(True)
weapons.remove(3)
print(weapons)
print('plazma' in weapons)
print('coconut' in weapons)
print(weapons[0:2])
print(type(weapons))

# кортеж
ryad1 = 1, 2, 3, 4, 5           # кортеж. неизменяемый список
ryad2 = (10, 9, 8, 7)           # занимают в памяти меньше места
ryad3 = tuple([11, 12, 13, 14])
print(ryad1)
print(ryad1[0])
print(ryad2)
print(ryad3)
print(type(ryad1))
print(ryad1.__sizeof__())

# но может хранить в себе изменяемые объекты

ryad_v = ([1, 2], 0)
print(ryad_v)
ryad_v[0][0] = 8
print(ryad_v)

# поддерживает контикенацию, сложение
# и умножение
print(ryad1+ryad2)
print(ryad3*3)
print(len(ryad3))
'''