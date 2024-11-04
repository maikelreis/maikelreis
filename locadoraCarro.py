import os
import time

os.system("cls")

print("=================")
print("")
print("Bem vindo a MSR Locadora de carros")
print("")
print("=================")
print("")
print("Escolha uma das opções abaixo:")

op_loc = {"0":"Mostra Portifolio","1":"Alugar um carro","2":"Devolver um carro","3":"Adicionar Carro"}
portifolio_carros={'carros':["Chevrolet Onix"],'diaria':["90"]}
carros_alugados={'carros':[],'diaria':[]}

def adicionar_carro(portifolio_carros):
    os.system("cls")
    print("====================================================")
    print("Você esta na sessão de adicionar carro ao portifólio")
    print("Gostaria de adicionar um novo carro?")
    print("1 - Sim")
    print("2 - Voltar menu principal")
    add_opt=int(input())

    if add_opt==2:
        return
    else:
        print("")
        print("Insira o os dados do carro")
        print('---------------------------')
        print('---------------------------')
        print("")
        print('Marca e Model do Carro:')
        carro=input()
        print('Qual o valor da diária em R$:')
        diaria=input()
        portifolio_carros["carros"].append(carro)
        portifolio_carros["diaria"].append(diaria)
    return

def mostrar_portifolio(portifolio_carros,carros_alugados):
    os.system("cls")
    print("====================================================")
    print("Você esta na sessão de Portifólio, abaixo segue os carros disponíveis no momento:")
    if portifolio_carros["carros"] != []:
        i=0
        for carro,diaria in zip(portifolio_carros['carros'],portifolio_carros['diaria']):
            print("{} - {} - R$ {} / dia".format(i,carro,diaria))
            i = i + 1
        print("")
        print("Selecione uma opção abaixo")
        print("1 - Alugar um carro")
        print("2 - Voltar ao menu principal")
        print('3 - Sair')
        op_select = int(input())
        if op_select == 1:
            print("")
            print("Qual carro da lista gostaria de alugar? - Informe o numero:")
            carro_select = int(input())
            aluguel_carro = list(portifolio_carros["carros"])[carro_select]
            aluguel_tarifa = list(portifolio_carros["diaria"])[carro_select]
            alugar_carro(carros_alugados,portifolio_carros,aluguel_carro,int(aluguel_tarifa),carro_select)
        elif op_select == 2:
            os.system("cls")
            return
        elif op_select == 3:
            exit()
        else:
            exit()
        return
    else:
        print("")
        print("-------------------------------------------------")
        print("Nenhum Carro disponivel no portifólio no momento.")
        print("-------------------------------------------------")
        print("")
        print("Selecione uma opção abaixo:")
        print("1 - Adicionar um carro")
        print("2 - Voltar menu principal")
        print("2 - Sair")
        op_select=int(input())
        if op_select == 1:
            adicionar_carro(portifolio_carros)
        elif op_select == 2:
            os.system("cls")
            return
        elif op_select == 3:
            exit()
        else:
            exit()

def alugar_carro(carros_alugados,portifolio_carros,aluguel_carro,aluguel_tarifa,carro_select):
    os.system("cls")
    print("====================================================")
    print("Você esta na sessão de aluguel")
    print("O carro escolhido foi: {}".format(aluguel_carro))
    print("")
    print("Quantos dias gostaria de alugar?")
    aluguel_dias = int(input())
    total_reserva = aluguel_dias * aluguel_tarifa
    print("Certo...Estamos reservando o carro para você, aguarde um instante...")
    time.sleep(2)
    print("")
    print("Resumo da reserva:")
    print("Carro escolhido {} por {} dias fica um total de R$ {}".format(aluguel_carro,aluguel_dias,total_reserva))
    print("")
    print("Confirma a reserva?")
    print("1 - Sim")
    print("2 - Não")
    op_select = int(input())
    if op_select == 2:
        print("")
        print("Certo.. Selecione uma das opções abaixo")
        print("1 - Escolher outro carro")
        print("2 - Voltar menu principal")
        print("3 - Sair")
        op_select2 = int(input())
        if op_select2 == 1:
            mostrar_portifolio(portifolio_carros)
        elif op_select2 == 2:
            os.system("cls")
            return True
        elif op_select2 == 3:
            exit()
        else:
            exit()
    else:
        time.sleep(2)
        print("")
        print("Reserva realizada com sucesso..")
        print("Aproveite bem seu veiculo, boa Viagem!!!")
        time.sleep(5)
        carros_alugados["carros"].append(aluguel_carro)
        carros_alugados["diaria"].append(str(aluguel_tarifa))
        portifolio_carros["carros"].pop(carro_select)
        portifolio_carros["diaria"].pop(carro_select)
        os.system("cls")
    return
    
def devolver_carro(carros_alugados,portifolio_carros):
    os.system("cls")
    print("====================================================")
    print("Você esta na sessão de Devolução de Carros")
    print("Qual carro você está devolvendo:")
    if carros_alugados["carros"] != []:
        i=0
        for carro,diaria in zip(carros_alugados['carros'],carros_alugados['diaria']):
            print("{} - {} - R$ {} / dia".format(i,carro,diaria))
            i = i + 1
        print("")
        print("Selecione o carro de devolução")
        carro_select = int(input())
        carro_devolvido = carros_alugados['carros'][carro_select]
        portifolio_carros["carros"].append(carros_alugados["carros"][carro_select])
        portifolio_carros["diaria"].append(carros_alugados["diaria"][carro_select])
        carros_alugados["carros"].pop(carro_select)
        carros_alugados["diaria"].pop(carro_select)
        print("")
        print("Aguarde, estamos processando sua devolução....")
        time.sleep(2)
        print("Obrigado.... Carro {} devolvido com sucesso".format(carro_devolvido))
        print("")
        print("Selecione opção desejada:")
        print("1 - Voltar Menu principal")
        print("2 - Sair")
        op_select = int(input())
        if op_select == 1:
            os.system("cls")
            return
        elif op_select == 2:
            exit()
        else:
            exit()
    else:
        print("")
        print("-------------------------------------------------")
        print("Nenhum Carro disponivel para devolução no momento.")
        print("-------------------------------------------------")
        print("")
        print("Selecione uma opção abaixo:")
        print("1 - Adicionar um carro")
        print("2 - Sair")
        op_select=int(input())
        if op_select == 1:
            adicionar_carro(portifolio_carros)
        elif op_select == 2:
            exit()
        else:
            exit()
          
while True:
    print("")
    print("====================================================")
    print("Menu Principal")
    for opt,tipo in op_loc.items():
        print("{} - {}".format(opt,tipo))
    op_select = int(input())
    if op_select not in (0,1,2,3):
        print("Selecione uma das opções acima")
    else:
        if op_select == 0:
            mostrar_portifolio(portifolio_carros,carros_alugados)
        elif op_select == 1:
            print("")
            print("Você será redirecionado para Sessão de portifólio para escolher um de nossos carros disponiveis...")
            time.sleep(2)
            mostrar_portifolio(portifolio_carros,carros_alugados)
        elif op_select == 2:
            devolver_carro(carros_alugados,portifolio_carros)
        elif op_select == 3:
            adicionar_carro(portifolio_carros)

