risc1 = [ 4.24 * 15
         ,2.88 * 6
         ,1.50 * 3]
         
qtd_pecas = 60
larg = 1.60
gram = 0.217

aparas = 3.435
linear = 0.217 * 1.62


total = risc1 + risc2 + risc3
kilos = total * linear



media = total / qtd_pecas
medKilos = kilos / qtd_pecas
print(f'{total} metros media de {media} por peca')
input()

