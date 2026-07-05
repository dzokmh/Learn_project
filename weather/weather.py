def check_t(t):
    if t <= 0:
        return f"{t} — Холодно"
    elif t <= 15:
        return f"{t} — Прохолодно"
    elif t <= 25:
        return f"{t} — Гарна погода"
    else:
        return f"{t} — Спекотно"

#temp = int(input("Введіть температуру на вулиці: "))

temperatures = [15, -3, 27, 8, 32, 0, 21]

for temp in temperatures:
    print(check_t(temp))
with open("weather.txt", "w") as f:
    for temp  in temperatures :
        f.write(f"{check_t(temp)}\n")
