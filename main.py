#создать кортеж с цифрами от 0 до 9 и посчитать сумму
import random
list=[]
for i in range(10):
    list.append(random.randint(0,10))
list=tuple(list)
print(list)
print(sum(list))

#выведите статистику частности букв в кортеже long_word
long_word=('t','t','a','u','u','a','u','u','u','t','t','a','u','u','u','u','u','t','u')
print('Статистика частности буквы "а":',long_word.count('a'))
print('Статистика частности буквы "t":',long_word.count('t'))
print('Статистика частности буквы "u":',long_word.count('u'))


