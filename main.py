#1
print("Задание №1")
a  = "Слово"
print(a[2])
print(a[-2])
print(a[0:5])
print(a[0:-2])
print(a[0::2])
print(a[1::2])
print(a[::-1])
print(a[::-2])
print(len(a))

#2
print("Задание №2")
s = input()
x = len(s)
l = x - x // 2
print(s[l:] + s[:l])

#3
print("Задание №3")
s = input()
a = s[:s.find('h')]
b = s[s.find('h'):s.rfind('h') + 1]
c = s[s.rfind('h') + 1:]
s = a + b[::-1] + c
print(s)
#4
print("Задание №4")
s = input()
if s.count('f') == 1:
    print(s.find('f'))
elif s.count('f') >=2:
    print(s.find('f'), s.rfind('f'))

#5
print("Задание №5")
a = input()
while True:
    b = input()
    if a[-1] != b:
        print(b)
        break
    else:
        a = b

#6
print("Задание №6")
line = input()
print(''.join(s * (line.index(s) + 1) for s in line))

#7
print("Задание №7")
s = input()
a = s[1::].replace('V', '!V!').split('!')
current_pos = 0
k = 1 if len(s) == 1 or s[1] == 'V' else 0
for i in a:
    if i == '':
        continue
    elif i[0] == '<':
        current_pos -= len(i)
        print(current_pos * ' ' + s[0]  + i.replace('<', s[0]))
        k = 0
    elif i[0] == '>':
        print(current_pos * ' ' + s[0]  + i.replace('>', s[0]))
        current_pos += len(i)
        k = 0
    elif i[0] == 'V':
        if k :
            print(current_pos * ' ' + s[0])
        k = 1
if k :
    print(current_pos * ' ' + s[0])

#8
print ("Задание №8")
s = input()
if len(s) % 2 == 0:
    n = len(s) // 2
    for i in range(n):
        print(' ' * (n - i - 1) + s[n - i - 1] + ' ' * i +
              ' ' * i + s[n + i])
else:
    d = (len(s) + 1) // 2
    print(' ' * ((len(s) - 1) // 2) + s[d - 1] + ' ' * ((len(s) - 1) // 2))
    for i in range(1, d):
        print(' ' * (d - i - 1) + s[d - i - 1] + ' ' * i +
              ' ' * (i - 1) + s[d + i - 1])

#9
print("Задание №9")
a = input().split()
for i in range(len(a)-1):
    n = int(a[i])
    i += 1
    m = int(a[i])
    if m > n:
        n = m
        print(m, end=' ')

#10
print("Задание №10")
a = input().split()
for i in range(len(a)-1):
    n = int(a[i])
    i += 1
    m = int(a[i])
    if (n * m) > 0:
        print(n, m, end=' ')
        break

#11
print("Задание №11")
a = [int(s) for s in input().split()]
if len(a) % 2 != 0:
    for i in range (0, len(a) - 1, 2):
        a[i], a[i + 1] = a[i + 1], a[i]
else:
    for i in range (0, len(a), 2):
      a[i], a[i + 1] = a[i + 1], a[i]
print(' '.join([str(i) for i in a]))

#12
print("Задание №12")
a = [int(s) for s in input().split()]
for i in a:
    if a.count(i) == 1:
        print(i, end=' ')
    else:
        continue
#13
print("Задание №13")
a = (map(int, input().split()))
b = list(map(str.lower,input().split()))
print(' '.join([b[i-1] for i in a]).capitalize())

#14
print("Задание №14")
x = []
y = []
no_yes = 0
n = 8
for i in range(n):
    new_element = [int(s) for s in input().split()]
    x.append(new_element[0])
    y.append(new_element[1])
for i in x:
    if x.count(i) > 1:
        no_yes += 1
for i in y:
    if y.count(i) > 1:
        no_yes += 1
for i in range(n):
    for j in range(i + 1, n):
        if abs(x[i] - x[j]) == abs(y[i] - y[j]):
            no_yes += 1
if no_yes == 0:
    print('NO')
else:
    print('YES')

#15
print("Задание №15")
lit = []
for i in range(int(input())):
    s = input()
    if 'Кто' in s:
        d = s[19:-1]
        sd = f'Заходит {d}!'
        lit.append(sd)
    elif 'только' in s:
        d = s[23:-1]
        sd = f'Заходит {d}!'
        lit.insert(0, sd)
    elif 'Следующий!' in s:
        if len(lit) != 0:
            print(*lit[0], sep='')
            lit.pop(0)
        else:
            print('В очереди никого нет.')
