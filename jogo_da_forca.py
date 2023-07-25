import random
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
    global palavra
    global chute_mencionado
    global tamanho
    global jogo
    global todas_letras_mencionadas
    palavra_para_chute = ["jooj"]
    palavra = random.choice(palavra_para_chute)
    tamanho = len(palavra)
    contador = 0
    mostrador = '_' * tamanho
    chute_mencionado = []
    jogo = ""
    todas_letras_mencionadas = []


# Loop para reexecutar o jogo quando após sua finalização:
def jogo_loop():
    global jogo
    # jogo = input("Gostaria de continuar ?\ns = sim, n = não\n")
    while jogo != ["S", "s", "n", "N"]:
        jogo = input("Gostaria de continuar ?\ns = sim, n = não\n")
        if jogo == "s" or "S":
            main()
            jogo_da_forca()
        elif jogo == "n" or "N":
            print("Obrigado por Jogar! \n Desenvolvido por Guilherme Silveira")
            exit()


def jogo_da_forca():
    global contador
    global mostrador
    global palavra
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

    elif chute in palavra:
        chute_mencionado.extend([chute])
        indicie = palavra.find(chute)
        palavra = palavra[:indicie] + "_" + palavra[indicie + 1:]
        mostrador = mostrador[:indicie] + chute + mostrador[indicie + 1:]
        print(mostrador + "\n")

    elif chute in chute_mencionado:
        print("Letra já mencionada, tente outra vez\n")

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
            print("Wrong guess. " + str(limite - contador) + " guesses remaining\n")
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
            print("Wrong guess. " + str(limite - contador) + " guesses remaining\n")
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
            print("Wrong guess. " + str(limite - contador) + " guesses remaining\n")
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
            print("Wrong guess. " + str(limite - contador) + " last guess remaining\n")
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
            print("Wrong guess. You are hanged!!!\n")
            print("The palavra was:", chute_mencionado, palavra)
            jogo_loop()

    if palavra == '_' * tamanho:
        print("Parabens! Você descobriu a palavra!")
        jogo_loop()

    elif contador != limite:
        jogo_da_forca()


main()

jogo_da_forca()

