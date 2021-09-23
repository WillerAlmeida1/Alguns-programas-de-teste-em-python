from random import sample as s
for n in range(int(input("quantos palpites  quer gerar?"))):
    print(sorted(s(range(1, 61), 6)))