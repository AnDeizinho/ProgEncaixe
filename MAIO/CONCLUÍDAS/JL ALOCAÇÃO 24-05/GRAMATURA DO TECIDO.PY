PESO = 1.125
comp = 4.35
larg = 2.40
areaqd = comp * larg
gramatura = PESO / areaqd
linear = gramatura * larg
print(f"gramatura {gramatura}")
print(f"linear {linear}")
print("================desfalc=====================")
tec = 3 *2.60
tec += 3 * 3.10

print(f"peso restante = {tec * (0.180 * 2.40)}")
input()