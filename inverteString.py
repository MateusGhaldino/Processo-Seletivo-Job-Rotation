
def inverteString(str):
    s = "" 
    for i in str: 
        s = i + s
    return s

def main():
     #Realiza a entrada de dados em string e valida se é um Valor(inteiro) valido positivo;
    while True:
        entrada = input('\nForneça a string:')
        if entrada.isalpha():
            break
        else:
            print('\nInforme um valor válido!!!')
    print(inverteString(entrada))

if __name__ == '__main__':
    main()