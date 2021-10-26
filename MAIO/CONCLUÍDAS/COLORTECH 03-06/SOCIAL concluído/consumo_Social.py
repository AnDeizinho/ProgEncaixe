m_mg_curta = 1.20
gg_mg_curta = 1.43

m_mg_longa = 1.41
gg_mg_longa = 1.59

verde = m_mg_curta * 3
verde += gg_mg_curta * 2
verde += gg_mg_longa * 1

azul = m_mg_curta * 3
azul += gg_mg_curta * 1
azul += m_mg_longa * 2
azul += gg_mg_longa * 1 

vermelho = m_mg_curta * 3 
vermelho += gg_mg_curta * 2
vermelho += m_mg_longa * 2 

cinza = m_mg_curta * 2

branco = m_mg_curta * 2

vermelho += 7 * 0.12
vermelho += 5 * 0.12
print(f"verde {verde}")
print(f"azul {azul}")
print(f"vermelho {vermelho}")
print(f"cinza {cinza}")
print(f"branco {branco}")
input() 