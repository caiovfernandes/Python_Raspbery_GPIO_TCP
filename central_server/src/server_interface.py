from server import CONNECTIONS
import json

EQUIPAMENTOS = {
    1: "lampada01",
    2: "lampada02",
    3: "projetor",
    4: "ac",
    5: "alarme",
    6: "presenca",
    7: "fumaca",
    8: "janela",
    9: "porta",
    10: "contagem_in",
    11: "contagem_out",
}


def show_interface():
    print()
    print("--------------------------------")
    print("Selecione a opção desejada:")
    print("1 - Verificar salas conectadas")
    print("2 - Receber informação da sala")
    print("3 - Alterar estado equipamento")
    print("4 - Ligar Alarme")
    print("5 - Desligar Alarme")
    print("--------------------------------")
    print()
    return input()


def mostrar_informacoes_sala(sala_selecionada):
    message = {
        "operation": "get_informacoes_sala",
        "sala": str(sala_selecionada)
    }

    for connection in CONNECTIONS:
        connection.socket.sendall(str.encode(json.dumps(message)))


def verificar_salas_conectadas():
    for connection in CONNECTIONS:
        print(connection)


def atualizar_equipamento(equipamento_selecionado, estado_desejado, sala):
    message = {
        "operation": "set_informacoes_sala",
        "attribute": EQUIPAMENTOS[int(equipamento_selecionado)],
        "estado": str(estado_desejado),
        "sala": int(sala)
    }
    print(message)
    for connection in CONNECTIONS:
        connection.socket.sendall(str.encode(json.dumps(message)))


def main():
    while (1):
        selected_option = show_interface()
        if selected_option == '1':
            verificar_salas_conectadas()
        elif selected_option == '2':
            print("De qual sala você quer receber informacao? (1 ou 2)?")
            selecionado = input()
            if int(selecionado) not in [1, 2]:
                print("Valor incorreto para número da sala (1 ou 2)")
                return 1
            mostrar_informacoes_sala(selecionado)
        elif selected_option == '3':
            print("De qual sala você quer alterar o estado? (1 ou 2)?")
            sala_selecionada = input()
            if int(sala_selecionada) not in [1, 2]:
                print("Valor incorreto para número da sala (1 ou 2)")
                return 1
            print()
            print("--------------------------------")
            print("De qual equipamento você deseja alterar o estado?")
            print("1 - Lampada 1")
            print("2 - Lampada 2")
            print("3 - Projetor")
            print("4 - Ar Condicionado")
            print("5 - Janela")
            print("6 - Porta")
            print("--------------------------------")
            print()
            equipamento_selecionado = input()
            if int(equipamento_selecionado) not in [1, 2, 3, 4, 5, 6]:
                print("Valor incorreto para equipamento")
                return 1
            print(f"\nOpcao Selecionada: {EQUIPAMENTOS[int(equipamento_selecionado)]}\n\n")

            print("--------------------------------")
            print("O que deseja fazer com o equipamento?")
            print("1 - Ligar")
            print("2 - Desligar")
            print("--------------------------------")
            selecionado = input()
            if int(selecionado) not in [1, 2]:
                print("Valor incorreto para estado")
                return 1
            atualizar_equipamento(equipamento_selecionado, True if selecionado == "1" else False, sala_selecionada)
        elif selected_option == '4':
            print("De qual sala você quer ligar o alarme? (1 ou 2)?")
            sala_selecionada = input()
            if int(sala_selecionada) not in [1, 2]:
                print("Valor incorreto para número da sala (1 ou 2)")
                return 1

            atualizar_equipamento(5, True)
        elif selected_option == '5':
            print("De qual sala você quer desligar o alarme? (1 ou 2)?")
            selecionado = input()
            if int(selecionado) not in [1, 2]:
                print("Valor incorreto para número da sala (1 ou 2)")
                return 1

            atualizar_equipamento(5, False, sala_selecionada)