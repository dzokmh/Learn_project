def check_t(t):
    city = t["city"]
    temp = t["temp"]

    if temp <= 0:
        return f"{city}:{temp}°C — Холодно"
    elif temp <= 15:
        return f"{city}:{temp}°C — Прохолодно"
    elif temp <= 25:
        return f"{city}:{temp}°C — Гарна погода"
    else:
        return f"{city}:{temp}°C — Спекотно"
temperatures = [
    {"city": "Київ",   "temp": 15},
    {"city": "Львів",  "temp": -3},
    {"city": "Одеса",  "temp": 27},
]

for temp in temperatures:
    print(check_t(temp))
