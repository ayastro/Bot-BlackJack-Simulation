import random

# Função para criar o baralho
def criar_baralho():
    naipes = ['Copas', 'Ouros', 'Paus', 'Espadas']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    baralho = [(v, n) for n in naipes for v in valores]
    random.shuffle(baralho)
    return baralho

# Função para calcular o valor da mão
def calcular_valor_mao(mao):
    valor = 0
    ases = 0
    for carta, naipe in mao:
        if carta in ['J', 'Q', 'K']:
            valor += 10
        elif carta == 'A':
            valor += 11
            ases += 1
        else:
            valor += int(carta)
    
    # Corrigir valor se houver Ases e a pontuação estourar 21
    while valor > 21 and ases:
        valor -= 10
        ases -= 1
    return valor

# Função para exibir a mão
def mostrar_mao(jogador, mao):
    print(f"{jogador} tem: ", ", ".join([f"{carta} de {naipe}" for carta, naipe in mao]))

# Função principal do jogo de Blackjack
def jogar_blackjack():
    # Criar e embaralhar o baralho
    baralho = criar_baralho()
    
    # Distribuir cartas para o jogador e dealer
    mao_jogador = [baralho.pop(), baralho.pop()]
    mao_dealer = [baralho.pop(), baralho.pop()]
    
    # Mostrar cartas iniciais
    mostrar_mao("Jogador", mao_jogador)
    print(f"Dealer mostra: {mao_dealer[0][0]} de {mao_dealer[0][1]}")
    
    # Turno do jogador
    while True:
        valor_jogador = calcular_valor_mao(mao_jogador)
        if valor_jogador == 21:
            print("Blackjack! Você ganhou!")
            return
        elif valor_jogador > 21:
            print("Você estourou! Dealer vence.")
            return
        
        acao = input("Você quer 'bater' ou 'ficar'? ").lower()
        if acao == 'bater':
            mao_jogador.append(baralho.pop())
            mostrar_mao("Jogador", mao_jogador)
        elif acao == 'ficar':
            break
        else:
            print("Comando inválido. Digite 'bater' ou 'ficar'.")

    # Turno do dealer
    print("\nTurno do Dealer:")
    mostrar_mao("Dealer", mao_dealer)
    while calcular_valor_mao(mao_dealer) < 17:
        mao_dealer.append(baralho.pop())
        mostrar_mao("Dealer", mao_dealer)
    
    valor_dealer = calcular_valor_mao(mao_dealer)
    valor_jogador = calcular_valor_mao(mao_jogador)

    # Resultados finais
    print("\nResultado Final:")
    mostrar_mao("Jogador", mao_jogador)
    mostrar_mao("Dealer", mao_dealer)
    
    if valor_dealer > 21:
        print("Dealer estourou! Você ganhou!")
    elif valor_jogador > valor_dealer:
        print("Você venceu!")
    elif valor_jogador < valor_dealer:
        print("Dealer venceu!")
    else:
        print("Empate!")

# Executar o jogo
if __name__ == "__main__":
    jogar_blackjack()