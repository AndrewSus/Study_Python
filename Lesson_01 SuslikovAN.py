#1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и
# сохраните в переменные, выведите на экран.

a = 2
#print(a)
print(a, type(a))

b = "Hello world"
#print(b)
print(b, type(b))

#c = input('Как тебя зовут? - ')
# print(a)
#print(c, type(c))

#d = input('Ведите  целое число - ')
#print(d, type(d))
#d = int(d) # Переведём в другой тип
print("Переведём в другой тип: ")
#print(d, type(d))

# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

e = input('Введите количество секунд, а я выведу в формате чч:мм:сек (не более 86400):  ')
#print(e, type(e))
#print(len(e))
if int(e)>86399:
    print("Это больше 24 часов. Алгоритм не будет корректно работать")
e = int(e)
#print(e, type(e))
h = e//3600 #Количество целых часов
varh = h * 60 #Количество минут в целых часах
m = (e - (varh * 60))//60 #Количество целых минут
varm = m*60 #Количество секунд в целых минутах
s = e - (varh * 60) - varm #Количество секунд
#print(h, m, s)
print (f"{h:02d}:{m:02d}:{s:02d}")

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
a = input("Введите число от 1 до 9 -  ")
a1 = a
a1 = int(a1)
a2 = a+a
a2 = int(a2)
a3 = a+a+a
a3 = int(a3)
n = a1 + a2 + a3
print("Сумма чисел n + nn + nnn = ", n)

# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте
# цикл while и арифметические операции.
# Вариант 1
''' a = list(input("Введите целое положительное число -  "))
#print(len(a))
#x = len(a)
#print(a[0])
arr = []
i = 0
while 0 <= len(a):
    #print(a[i])
    arr.extend(a[i])
    i += 1
    print(arr)
print(max(arr) '''


# Вариант 2:
a = input("Введите целое положительное число -  ")
print(a, type(a))
max(a)



 # 5.  Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

a = int(input("Сообщите выручку -  "))
b = int(input("Сообщите Ваши издержки  -  "))
if a > b:
    print("Вы сработали с прибылью", a-b, " руб")
    c = int(input("Сообщите численность сотрудников - "))
    print("Прибыль в расчете на одного сотрудника составляет:  ",(a-b)/c, " руб")
else:
    print("Ваш убыток составляет:", b-a, " руб")



# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день
# спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который общий
# результат спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b и выводить
# одно натуральное число — номер дня.



