def si_es_Bisiesto (anyo):
    return (anyo %4 == 0 and (anyo % 100 != 0 or anyo %400 == 0))


dia = int(input("Dime un día:\n"))
mes = int(input("Dame un mes:\n"))
anyo = int(input("Dame un año:\n"))

meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if si_es_Bisiesto(anyo):
    meses [1] = 29

dia += 1
if dia > meses[mes - 1]:
    dia = 1
    mes += 1
    if mes > 12:
        mes = 1
        anyo += 1
print(f"{dia} {mes} {anyo}")

