n = 0
i = 1

for _ in range(1, 65):
    n = n + i
    i = i * 2

print(f"国际象棋64个格子中总的麦粒数量为： {n}")
