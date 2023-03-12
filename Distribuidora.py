"""
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde 
calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.
"""


Sp = 67836.43
Rj = 36678.66
Mg = 29229.88
Es = 27165.48
Outros = 19849.53

valoresEstados  =  [67836.43, 36678.66, 29229.88, 27165.48, 19849.53]
nomeEstados = ['São Paulo', 'Rio de Janeiro', 'Minas Gerais', 'Espirito Santo', 'Outros Estados']

def calculaPercentual (valorTotal):
    posicao = 0
    percentual = 0
    for valorEstado in valoresEstados:
        percentual = (valorEstado/valorTotal) * 100
        percentual = round(percentual,2)
        print('\nO percentual de {0} foi de {1}%.'.format(nomeEstados[posicao], percentual))
        posicao += 1


def main():
    valorTotal = Sp + Rj + Mg + Es + Outros
    calculaPercentual(valorTotal)


if __name__ == '__main__':
    main()