
l = int(input('задайте длинну списка - '))
sp = []
a = int(0)
for i in range(l):
    n = int(input('Введите целое число - '))
    sp.append(n)
    if i % 2 == 0:
        a = int(a + n)
print(f'список элементов - {sp}')
print(f'сумма нечетных элементов равна - {a}')

sp1 = []
b = int(0)
d = float(0)
if len(sp)%2 == 0:
    for i in range(len(sp)//2):
        b = sp[i]*sp[-i-1]
        sp1.append(b)
    print(f'cписок произведений пар равноудалённых чисел - {sp1}')
else:
    for i in range((len(sp)-1) // 2):
        b = sp[i] * sp[-i - 1]
        sp1.append(b)
    d = sp[len(sp)//2+(1//2)]*2
    sp1.append(d)
    print(f'cписок произведений пар равноудалённых чисел - {sp1}')


from decimal import Decimal
ls = int(input('задайте длинну списка - '))
listfl = []
listfl1 = []
listfl2 = []
x = float
x2 = int
n1 = float(0)
for i in range(ls):
    fl = str(input('Введите вещественное число - '))
    listfl.append(fl)
    if fl.find('.') > 0:
         # fl = fl.split('.')
         x = float(fl) - int(fl[0])
         listfl1.append(x)
for i in listfl1:
    n1 = float(i)
    if n1 != 0:
        listfl2.append(n1)
listfl2.sort()
n2 = listfl2[-1] - listfl2[0]
print(f'Спиок чисел - {listfl}')
print(f'Разница между макимальной и минимальной величиной дробной части равняетя -{n2}')




bi = int(input('Введите целое число - '))
bilist = []
bilist1 = str
n = bi
x = int
while bi != 0:
    if bi%2 > 0:
        x = 1
        bilist.append(x)
    else:
        x = 0
        bilist.append(x)
    bi = int(bi // 2)
bilist.reverse()
bilist1 = str(bilist).replace(', ', '')
if n == 0:
    print(' запись в двоичном коде - 0')
else:
    print(f' запись в двоичном коде - {bilist1} ')


f = int(input('Задайте число элементов для чисел Фибоначе больше двух - '))
fib = [0, 1]
fib2 = []
fib4 = []
fn = int
for i in range(2, (f+1)):
    fn = fib[i-1]+fib[i-2]
    fib.append(fn)
    fib4.append(fn)
    fn = ((-1)**(i+1))*(fib[i])
    fib2.append(fn)
fib2.reverse()
fib2.append(1)
fib4 = fib2 + fib

print(f'Список чисел Фибоначе {fib4}')


