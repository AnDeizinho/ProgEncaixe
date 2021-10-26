def consumo_malha (LINEAR, METROS):
    return METROS * LINEAR
def consumo_plano(folhas, comp):
    return folhas * comp
    
riscos = [consumo_plano(4, 3.50), 
          consumo_plano(2, 1.24)]
print("total ", sum(riscos))
ris = [3.53 * 4 , 2.38 * 1]
for i in ris :
    print(i)

print(sum(ris))
input()

    