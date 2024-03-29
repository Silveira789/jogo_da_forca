import random
import sys
import time

# Inicio do jogo
print("Bem vindo ao jogo da forca")
name = input("Digite seu nome: ")
print(f"Olá {name}! Boa sorte!")
time.sleep(2)
print("O jogo irá começar, você tem 5 tentativas")
print()


# Parâmetros requeridos para execução do jogo - inicialização das variáveis
def main():
    global contador
    global mostrador
    global palavra_sorteada
    global chute_mencionado
    global tamanho
    global jogo
    global todas_letras_mencionadas
    global palavra_view
    palavra_para_chute = ["cola", "laranja", 'caneta', 'azul', 'mato', "beijo", "calor", "polvo", "brasil", "bela", "horizonte"]
    palavra_sorteada = random.choice(palavra_para_chute)
    palavra_view = palavra_sorteada
    tamanho = len(palavra_sorteada)
    contador = 0
    mostrador = '_' * tamanho
    chute_mencionado = []
    jogo = ""
    todas_letras_mencionadas = []


# Loop para reexecutar o jogo quando após sua finalização:
def jogo_loop():
    jogo = ''
    while jogo.lower() not in ["s", "n"]:
        jogo = input("Gostaria de continuar ?\ns = sim, n = não\n")
        if jogo == "s":
            main()
            jogo_da_forca()
        elif jogo == "n":
            print("Obrigado por Jogar! \n Desenvolvido por Guilherme Silveira")
            sys.exit()


def jogo_da_forca():
    global contador
    global mostrador
    global palavra_sorteada
    global chute_mencionado
    global jogo
    global todas_letras_mencionadas


    limite = 5
    chute = input(f"Está é a palavra secreta: {mostrador}\nDigite a letra sugerida: ")
    todas_letras_mencionadas.extend([chute])
    chute = chute.strip()

    if len(chute.strip()) == 0 or len(chute.strip()) >= 2 or chute <= "9":
        print("Opção inválida, tente outra letra\n")
        jogo_da_forca()

    elif chute in palavra_sorteada:
        chute_mencionado.extend([chute])
        indicie = palavra_sorteada.find(chute)
        palavra_sorteada = palavra_sorteada[:indicie] + "_" + palavra_sorteada[indicie + 1:]
        mostrador = mostrador[:indicie] + chute + mostrador[indicie + 1:]
        print(mostrador + "\n")
        print(f"Letras mencionadas: {todas_letras_mencionadas}")



    elif chute in chute_mencionado:
        print()
        print("Letra já mencionada, tente outra vez\n")
        print()

    else:
        contador += 1

        if contador == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Palpite errado. " + str(limite - contador) + " chances restantes\n")
            print()
            print(f"Letras mencionadas: {todas_letras_mencionadas}")
            print("========================================================================")

        elif contador == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Palpite errado. " + str(limite - contador) + " chances restantes\n")
            print()
            print(f"Letras mencionadas: {todas_letras_mencionadas}")
            print("========================================================================")


        elif contador == 3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Palpite errado. " + str(limite - contador) + " chances restantes \n")
            print()
            print(f"Letras mencionadas: {todas_letras_mencionadas}")
            print("========================================================================")


        elif contador == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Palpite errado. " + str(limite - contador) + " chance restante\n")
            print()
            print(todas_letras_mencionadas)
            print("========================================================================")


        elif contador == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Chute errado. Você perdeu!!!\n")
            print("A palavra era:", palavra_view)
            jogo_loop()

    if palavra_sorteada == '_' * tamanho:
        print("Parabens! Você descobriu a palavra!")
        jogo_loop()

    elif contador != limite:
        jogo_da_forca()


# Execução de jogo

main()

jogo_da_forca()

jogo_loop()
