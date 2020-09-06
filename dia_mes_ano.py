def idade(dia,mes,ano,diap,mesp,anop):
    idade= ano - anop
    if mes<=mesp:
        idade = idade - 1
        print(f'{idade}')
    else:
        print(f'{idade}')
def main():
    dia=int(input(''))
    mes=int(input(''))
    ano=int(input(''))
    diap=int(input(''))
    mesp=int(input(''))
    anop=int(input(''))
    idade(dia,mes,ano,diap,mesp,anop)
if __name__=='__main__':
    main()

    
    
