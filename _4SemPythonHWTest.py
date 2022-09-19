from random import randint
import itertools
import math
from math import pi
#1.Вычислить число c заданной точностью d

#Пример:

#- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

#При реализации многих численных методов точность вычислений зависит от числа шагов. 
#Однако за какое именно число шагов будет достигнута приемлемая точность, заранее сказать трудно и желательно, 
#чтобы программа сама определяла, когда следует остановиться.



n = pi
print(n)
n = int(input("Введите число: "))
my_pi = sum(1/16**x*(4/(8*x + 1) - 2/(8*x + 4) - 1/(8*x + 5) - 1/(8*x + 6)) for x in range(n))
print(my_pi)

#2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.



n = int(input())
i = 2
while n > 1:
    while n % i == 0:
        print(i, end=' ')
        n //= i
    i += 1
    
#3.Задайте последовательность чисел. 
#Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

lst = list(map(int, input("Input numbers with space:\n").split()))
print(f"Original list: {lst}")
new_lst = []
[new_lst.append(i) for i in lst if i not in new_lst]
print(f"Unique list of elements: {new_lst}")

# 4.Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.    
#     *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x²



k = randint(2, 7)

# Второй многочлен для следующей задачи:

k = randint(2, 5)

ratios = get_ratios(k) 
polynom2 = get_polynomial(k, ratios)
print(polynom2)

with open('33_Polynomial2.txt', 'w') as data:
    data.write(polynom2)

def get_ratios(k):
    ratios = [randint(0, 10) for i in range (k + 1)]
    while ratios[0] == 0:
        ratios[0] = randint(1, 10) 
    return ratios

def get_polynomial(k, ratios):
    var = ['*x^']*(k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') if a !=0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(itertools.chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x',' x')


ratios = get_ratios(k)
polynom1 = get_polynomial(k, ratios)
print(polynom1)

with open('33_Polynomial.txt', 'w') as data:
    data.write(polynom1)
