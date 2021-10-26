def TotalMetro(comp, folhas):
    return comp * folhas
cip24 = sum(
            [
                TotalMetro(3.18, 8),
                TotalMetro(1.18, 4)
            ])

cip25 = sum([TotalMetro(4.83, 4)])

cip26 = TotalMetro(2.99, 4)

det_verm = TotalMetro(0.77, 4)
print(f'primeiro {cip24} segundo {cip25} terceiro {cip26}')
print(f'{cip24 + cip25 + cip26} metros de unisoft azul royal')
print(f'{det_verm} metros para manga vermelha')
input()
