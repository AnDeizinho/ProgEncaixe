def unistil():
    feminino = 2*2.64
    masc = 2 * 4.15
    masc += 9 * 2.37
    masc += 1 * 1.19
    return feminino + masc
def vermelho():
    det_masc = 2.08
    det_fem = 0.84
    camisaria_verm = det_masc + det_fem
    camisaria_verm += 1.88
    camisaria_verm += 2.94
    return camisaria_verm
def ibiza():
    masc_ib = 6 * 4.06
    masc_ib += 2 * 4.05
    masc_ib += 5 * 2.28
    masc_ib += 1.90

    fem_ib = 4 * 5.05
    fem_ib += 2 * 1.24
    return fem_ib + masc_ib
def intertela():
    intretela = 0.60
    intretela += 3.06
    intretela += 0.23
    intretela += 1.35
    return intretela
   
print("unistil preto = ",unistil())
print("tricoline ibiza = ",ibiza())
print("detalhe vermelho = ", vermelho())
print("intretela = ", intertela())
input()

