def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

def sum(x, y):
    for i in range(len(M)):
        f = []

        for j in range(len(M[i])):
            f.append(y[M[i][j]])

        l = 0
        for k in range(len(f)):
            if f[k] == 1:
                l += 1
        if l % 2 == 0:
            l = 0
        else:
            l = 1
        x.append(l)

try:
    allreg = int(input("Введите количество регистров: "))
    allreg1 = allreg
    reg = [0] * allreg

    s = int(input("Введите количество сумматоров: "))
    M = []
    print("Введите перечень регистров для сумматора (через пробел):")
    for i in range(s):
        sumreg = input()
        sumreg = sumreg.split()
        for j in range(len(sumreg)):
            sumreg[j] = int(sumreg[j]) - 1
        M.append(sumreg)
except:
    print("Ошибка! Введите натуральное число.")
    exit()

line = input("\nВведите последовательность, которую необходимо закодировать: ")
line1 = line
pr1 = False
for i in range(len(line)):
    if line[i] != "0":
        if line[i] != "1":
            pr1 = True
            break
if pr1:
    line = text_to_bits(line)
print("\nИнформационное слово: ", line)
rez = []

while len(line) != 0 or allreg != 0:
    if len(line) != 0:
        reg.insert(0, int(line[0]))
        del reg[-1]
        line = line.replace(line[0], '', 1)
        sum(rez, reg)
    else:
        reg.insert(0, 0)
        del reg[-1]
        sum(rez, reg)
        allreg -= 1

REZ = ""
for i in range(len(rez)):
    REZ += str(rez[i])
print("Кодовое слово: ", REZ)

INFSL = []
while len(REZ) != 0:
    ck = ""
    for i in range(s):
        ck += REZ[0]
        REZ = REZ.replace(REZ[0], "", 1)

    reg1 = []
    for i in range(len(reg)):
        reg1.append(reg[i])
    reg1.insert(0, 0)
    del reg1[-1]

    rez1 = []
    sum(rez1, reg1)

    REZ1 = ""
    for i in range(len(rez1)):
        REZ1 += str(rez1[i])


    reg2 = []
    for i in range(len(reg)):
        reg2.append(reg[i])
    reg2.insert(0, 1)
    del reg2[-1]

    rez2 = []
    sum(rez2, reg2)

    REZ2 = ""
    for i in range(len(rez2)):
        REZ2 += str(rez2[i])


    if REZ1 == ck and REZ2 != ck:
        INFSL.append(0)
        reg = []
        for i in range(len(reg1)):
            reg.append(reg1[i])

    elif REZ1 != ck and REZ2 == ck:
        INFSL.append(1)
        reg = []
        for i in range(len(reg2)):
            reg.append(reg2[i])

    elif len(REZ) == 0:
        INFSL.append(0)


firstword = ""
for i in range(len(INFSL)):
    firstword += str(INFSL[i])
firstword = firstword[:-allreg1]
print("Изначальное информационное слово: ", firstword)
print("\nИзначальная последовательность: ", text_from_bits(firstword))

