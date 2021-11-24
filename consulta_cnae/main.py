from consulta_cnae import Cnae

def main():         
    cnae = str(input('Informe um Cnae: '))

    cnaes = Cnae(cnae)
    cnaes.result()

if __name__ == '__main__': 
    main()