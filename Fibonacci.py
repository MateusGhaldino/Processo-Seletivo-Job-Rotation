"""
Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

"""
#Recebe um valor inteiro positivo e retorna  para quando valor pertencer a serie Fibonacci e false para casos contrarios
def Fibonacci(numero):
    parada = numero
    anterior = 0
    proximo = 0

    while(proximo <= parada):

        if numero == proximo:
            return ('\nO valor ' + str(numero) + ' pertece a serie de Fibonacii.') 
        proximo = proximo + anterior
        anterior = proximo - anterior
        if(proximo == 0):
            proximo = proximo + 1

    return ('\nO valor ' + str(numero) + ' não pertece a serie de Fibonacii.') 

def main():

    #Realiza a entrada de dados em string e valida se é um Valor(inteiro) valido positivo;
    while True:
        entrada = input('\nForneça o numero:')
        if entrada.isdigit():
            break
        else:
            print('\nInforme um valor válido!!!')
    print(Fibonacci(int(entrada)))


if __name__ == '__main__':
    main()