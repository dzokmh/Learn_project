def check_t(t):
    if t <= 0:
        return f"{t} — Холодно"
    elif t <= 15:
        return f"{t} — Прохолодно"
    elif t <= 25:
        return f"{t} — Гарна погода"
    else:
        return f"{t} — Спекотно"

while True:
    try:
        temp = int(input("Введіть температуру на вулиці, числом: "))
        break
    except ValueError:
        print("Будь ласка введіть числове значення температури без літер")
print(check_t(temp))
