import json

"""
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
"""


def converteValores(lista):
    valores = []
    for val in lista:
        valores.append(float(val))
    return valores

def converteDias(lista):
    valores = []
    for val in lista:
        valores.append(int(val))
    return valores

#Abre o arquivo Json
def ler_json(arq_json):
    with open(arq_json, 'r', encoding='utf8') as f:
        return json.load(f)
    
#Verifica dentro da lista de valores qual foi o menor fatorameto do mês
def menorFaturamentoMes(vetorFaturamentoMensal):
    menorAux = vetorFaturamentoMensal[0]
    for FaturamentoDiario in vetorFaturamentoMensal:
        if FaturamentoDiario < menorAux:
            menorAux = FaturamentoDiario
    return ("\nO menor Faturamento registrado no mês foi de R$ {0}\n".format(menorAux))

#Verifica dentro da lista de valores qual foi o Maior fatorameto do mês
def maiorFaturamentoMes(vetorFaturamentoMensal):
    maiorAux = vetorFaturamentoMensal[0]
    for FaturamentoDiario in vetorFaturamentoMensal:
        if FaturamentoDiario > maiorAux:
            maiorAux = FaturamentoDiario
    return ("\nO maior Faturamento registrado no mês foi de R$ {0}\n".format(maiorAux))

#Verifica Número de dias no mês em que o valor de faturamento diário foi superior à média mensal
def maiorQueMediaMensal(vetorFaturamentoMensal):
    soma = 0
    dias = 0
    for valorDiario in vetorFaturamentoMensal:
        soma = valorDiario + soma

    media = soma/len(vetorFaturamentoMensal)
    print("\nValor da media mensal foi de R$ %.2f"% media)

    for valorDiario in vetorFaturamentoMensal:
        if media < valorDiario:
            dias += 1 
    
    return ("\nO número de dias no mês em que o valor de faturamento diário foi superior à média mensal foi de:{0}\n".format(dias))


def main():
    
    #Abre o arquivo .json que está no direito raiz que está com os dados do Faturamento mensal
    data = ler_json('faturamento.json')
   
    # Pegar as chaves de dentro de 'Faturamento' e 'Março' e jogar na variável 'keys'
    chaves = data['faturamento_Março']['Dias'].keys()
    valores = data['faturamento_Março']['Dias'].values()

    #Convertendo os valores em lista
    vetorDias = list(chaves)
    vetorFaturamentoMensal = list(valores)

    #Convertendo os valores da lista de str para int e float
    vetorDias = converteDias(vetorDias)
    vetorFaturamentoMensal = converteValores(vetorFaturamentoMensal)


    print(menorFaturamentoMes(vetorFaturamentoMensal))
    print(maiorFaturamentoMes(vetorFaturamentoMensal))
    print(maiorQueMediaMensal(vetorFaturamentoMensal))



if __name__ == '__main__':
    main()