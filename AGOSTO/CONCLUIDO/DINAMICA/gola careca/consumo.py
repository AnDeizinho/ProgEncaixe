risc1 = [ 3.58 * 30, 2.89 * 5, 3.55 * 2 , 1.48 * 1, 2.88 * 3]
         
qtd_pecas = 254+75
larg = 2.40
gram = 0.18

aparas = 8.240 + 2.535


linear = gram * larg
total = sum(risc1)
kilos = total * linear



media = total / qtd_pecas
medKilos = kilos / qtd_pecas
print(f'{qtd_pecas} pecas')
print(f'{total} metros e {kilos} kilos')
print(f'{media} Mt por peca e {medKilos} kl por peca')
print(f'{aparas} kilos de aparas, {(aparas /kilos)*100}% de perda')
input()

