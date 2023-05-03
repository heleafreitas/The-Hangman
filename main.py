from multiprocessing import Semaphore
import random
from multiprocessing.pool import ThreadPool
from time import sleep

# Palavras para o jogo
palavras = ['amor', 'fato', 'mito', 'caos', 'como', 'esmo', 'brio', 'vide', 'sede', 'pois', 'vida', 'auge', 'casa', 'saga', 'medo', 'ermo', 'suma', 'mote', 'idem', 'tolo', 'urge', 'sina', 'crer', 'apto', 'veio', 'pela', 'zelo', 'pude', 'tudo', 'ruim', 'rude', 'cota', 'coxo', 'soar', 'para', 'ater', 'mais', 'ente', 'amar', 'fase', 'auto', 'voga']
palavra = random.choice(palavras)
# Cria uma lista de semáforos para cada posição na palavra
semaforos = [Semaphore(1) for _ in range(4)]
posicoes = [True, True, True, True]
# Lista de jogadores e suas pontuações iniciais
jogadores = {'Jogador 1': 0, 'Jogador 2': 0, 'Jogador 3': 0}

# Função que cada thread do palpite irá executar
def palpite(args):
    jogador, letra, posicao = args
    # Espera a liberação do semáforo correspondente à posição da letra
    semaforos[posicao].acquire()
    # Verifica se a letra do palpite é igual à da posição correspondente na palavra
    if palavra[posicao] == letra:
        print(f'Analisando palpite do {jogador} da letra {letra} na posição {posicao}: acertou!')
        posicoes[posicao] = False
        # Acertou! Incrementa a pontuação do jogador
        jogadores[jogador] += 1
    # Libera o semáforo correspondente à posição da letra
    else:
        print(f'Analisando palpite do {jogador} da letra {letra} na posição {posicao}: errou!')
        semaforos[posicao].release()

def verificar_adivinhacao():
    adivinhacao = ''
    for i in range(4):
        if posicoes[i]:
            adivinhacao += '_'
        else:
            adivinhacao += palavra[i]
    print(f'Situação atual da adivinhação: {adivinhacao}')

# Loop principal do jogo
for rodada in range(5):
    pontos_totais = 0
    print(f'\n\tRodada {rodada+1} \n')
    # Mostra a situação da adivinhação da palavra
    verificar_adivinhacao()
    # Loop para os palpites dos jogadores
    palpites_jogadores = {}
    for jogador in jogadores.keys():
        print(f'Vez do {jogador}')
        palpites_jogador = []
        # Cada jogador faz 4 palpites aleatórios
        for i in range(4):
            letra = input('Escolha a letra: ')
            posicao = int(input(f'De 0 a 3, escolha uma posição para a letra {letra}: '))
            # Cria uma nova thread para o palpite
            palpites_jogador.append((jogador, letra, posicao))
        palpites_jogadores[jogador] = palpites_jogador
        print('\n')
     # Executa os palpites dos jogadores ao final da rodada
    with ThreadPool(processes=12) as pool: # Cria uma lista com todos os palpites dos jogadores
        args_list = []
        for palpites_jogador in palpites_jogadores.values():
            for palpite_jogador in palpites_jogador:
                args_list.append(palpite_jogador)
        pool.map_async(palpite, args_list)  # Executa as threads utilizando o método imap_unordered()
        sleep(2)
    print('\nPontuação:')
    for jogador, pontos in jogadores.items():  # Mostra a pontuação de cada jogador
        print(f'{jogador}: {pontos}')
        pontos_totais += pontos
    if pontos_totais >= 4:
        break

vencedor = max(jogadores, key=jogadores.get) # Verifica quem ganhou
print('\n\tO JOGO ACABOU!')
print(f'A palavra era: {palavra}')
print(f'O vencedor é {vencedor} com {jogadores[vencedor]} pontos!')