def check_t(t):
    if t <= 0:
        return "Холодно"
    elif t <= 15:
        return "Прохолодно"
    elif t <= 25:
        return "Гарна погода"
    else:
        return "Спекотно"

#temp = int(input("Введіть температуру на вулиці: "))

temperatures = [15, -3, 27, 8, 32, 0, 21]

for temp in temperatures:
    print(check_t(temp))
  
