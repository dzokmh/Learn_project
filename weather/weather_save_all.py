from pathlib import Path

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

with open("weather.txt", "w") as f:
    for temp in temperatures:
        result = check_t(temp)
        print(result)
        f.write(f"{result}\n")

