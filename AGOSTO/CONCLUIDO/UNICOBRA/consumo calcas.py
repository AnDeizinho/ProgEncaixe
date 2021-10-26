risc1 = [40 * 4.35, 10 *4.45 ]
         
qtd_pecas = 200
larg = 1.70
gram = 0.250

aparas = 20


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

