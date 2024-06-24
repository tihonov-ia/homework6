my_dict = {'Ivan' : 1981, 'Igor' : 1982, 'Petya' : 1983, 'Valentin' : 1984}
print('Dict:', my_dict)
print('Existing value:', my_dict.get('Ivan'))
print('Not existing value:', my_dict.get('Sasha'))
my_dict.update({'Konstantin' : 1985})
my_dict['Evgeny'] = 1986
a = my_dict.pop('Igor')
print('Deleted value:', a)
print('Modified dictionary:', my_dict)
#Пример результата выполнения программы:
#Dict: {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
#Existing value: 2002
#Not existing value: None
#Deleted value: 1999
#Modified dictionary: {'Vasya': 1975, 'Kamila': 1981, 'Artem': 1915, 'Masha': 2002}

my_set = {1,'Яблоко', 42.314}
print('Set:', my_set)
my_set.add(13)
a = (5,6,1.6)
my_set.add(a)
my_set.remove(1)
print('Modified dictionary:', my_set)
#Пример результата выполнения программы:
#Set: {1, 'Яблоко', 42.314}
#Modified set: {'Яблоко', 42.314, 13, (5, 6, 1.6)}
