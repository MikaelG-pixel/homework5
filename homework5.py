immutable_var = 1, 3.7, 7, True, 'Язь'
print(immutable_var)
print('Типы данных:')
print(type(immutable_var[0]))
print(type(immutable_var[1]))
print(type(immutable_var[2]))
print(type(immutable_var[3]))
print(type(immutable_var[4]))
# Изменить кортеж невозможно по определению из-за своиств саомого кортежа,
# однако если кортеж содержит в себе список заключенный в квадратные скобки [],
# то возможно изменять элементы списка включенные в кортеж
immutable_var_1 = 1, 3.7, 7, [True, 'Язь']
print(immutable_var_1)
immutable_var_1[3][0] = 'Рыба моей мечты'
print(immutable_var_1)

mutable_list = [1, 8.2, 'ЯЯЯЯЗЗЗЬЬ', False]
print(mutable_list)
mutable_list[0] = 17
print(mutable_list)
mutable_list.append('Это')
print(mutable_list)
mutable_list.extend('Карась')
print(mutable_list)
mutable_list.remove(8.2)
print(mutable_list)