num = 0
with open('love.txt', 'a', encoding='utf-8') as f:
    for i in range(10000):
        num += 1
        f.write(f"{num}) Я тебя люблю :3 \n")