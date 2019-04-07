# 2. Graduation

# Напишете програма, която изчислява средната оценка на ученик от цялото му обучение. На първия ред ще получите името
#  на ученика, а на всеки следващ ред неговите годишни оценки. Ученикът преминава в следващия клас, ако годишната му
# оценка е по-голяма или равна на 4.00. Ако оценката му е под 4.00, той ще повтори класа.
# При успешно завършване на 12-ти клас да се отпечата:
#  "{име на ученика} graduated. Average grade: {средната оценка от цялото обучение}"
# Стойността трябва да бъде форматирана до втория знак след десетичната запетая.

name = input()

grade = float(input())
counter = 0  # брояч
result = 0  # среден успех
year = 1

while year < 12:
    result += grade  # събира средния успех
    counter += 1  # леди колко пъти сме се въртяли в този цикъл

    if grade >= 4:
        year += 1

    grade = float(input())

print(f'{name} graduated. Average grade: {result / counter:.2f}')