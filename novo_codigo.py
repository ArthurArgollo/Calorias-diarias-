## Calculo de calorias diarias
def sexo():
    depois_Decido= input('''
Escolha M para maculino ou F para feminino
'''
    )
    if depois_Decido == "M":
        peso= int(input("Informe seu peso: "))
        altura= float(input("Informe sua altura: "))
        idade = int(input("informe sua idade: "))
        altura_cm = altura * 100
        Tmb = (10 * peso) + (6.25 * altura_cm) - (5 * idade) + 5
    elif depois_Decido == "F":
        peso= int(input("Informe seu peso: "))
        altura= float(input("Informe sua altura: "))
        idade = int(input("informe sua idade: "))
        altura_cm = altura * 100
        Tmb = (10 * peso) + (6.25 * altura_cm) - (5 * idade) - 161
    else:
        print("Digite a opção correta")
   
    escolha = input('''
Escolha o nível de atividade física que mais faz sentido com sua rotina:
                    
Sedentário (pouca ou nenhuma atividade fisica)               
Levemente ativo (exercício leve ou esportes 1-3 dias/semana)                
Moderadamente ativo (exercício moderado ou esportes 3-5 dias/semana)
Altamente ativo (exercício intenso ou esportes 6-7 dias/semana)
Extremamente ativo (exercício muito intenso, trabalho físico pesado)
'''
    )
    ## Sedentário
    if escolha == "Sedentário":
        Sedentario = (Tmb*1.2)
        ca = Sedentario
        print("Você deve ingerir {:.2f} calorias".format (ca))
    ## Levemente ativo
    elif escolha == "Levemente ativo":
        Levemente_ativo = (Tmb*1.375)
        ca = Levemente_ativo
        print("Você deve ingerir {:.2f} calorias".format(ca))
    ## Moderadamente ativo
    elif escolha == "Moderadamente ativo":
        Moderadamente_ativo = (Tmb * 1.55)
        ca = Moderadamente_ativo
        print("Você deve ingerir {:.2f} calorias".format(ca))
    ## Altamente ativo
    elif escolha == "Altamente ativo":
        Altamente_ativo = (Tmb * 1.725)
        ca = Altamente_ativo
        print("Você deve ingerir {:.2f} calorias".format(ca))
    ## Extremamente ativo
    elif escolha.upper() == "Extremamente ativo":
        Extremamente_ativo = (Tmb * 1.9)
        ca = Extremamente_ativo
        print("Você deve ingerir {:.2f} calorias".format(ca))
    else:
        print("Você não selecionou uma opção valida".format (dnv()))

    objetivo = input('''
Digite "ganhar" se seu objetivo for ganhar peso ou "perder" se seu objetivo for perder peso
'''
    )
    if objetivo == "ganhar":
        print("Você deve consumir {:.2f} calorias".format (ca + 500))
    elif objetivo == "perder":
        print("Você deve perder {:.2f} calorias".format (ca - 500))
    else:
        print("Digite a opção correta")
    dnv()

def dnv():
    novo_calc = input (
        '''Deseja continuar? Selecione "S" para sim ou "N" para não: '''
    )
    if novo_calc == "S":
        sexo()
    elif novo_calc == "N":
        print("A calculadora será finalizada.")
    else:
        dnv()
sexo()