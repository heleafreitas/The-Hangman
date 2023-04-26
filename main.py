import threading
import random
# from jogador import *

banco_de_palavras = ['amor', 'fato', 'mito', 'caos', 'como', 'esmo', 'brio', 'vide', 'sede', 'pois', 'vida', 'auge', 'casa', 'saga', 'medo', 'ermo', 'suma', 'mote', 'idem', 'tolo', 'urge', 'sina', 'crer', 'apto', 'veio', 'pela', 'zelo', 'pude', 'tudo', 'ruim', 'rude', 'cota', 'coxo', 'soar', 'para', 'ater', 'mais', 'ente', 'amar', 'fase', 'auto', 'voga']
palavra = random.choice(banco_de_palavras)
letras_adivinhadas = ["_", "_", "_", "_"]
semaforos = [threading.Semaphore(1) for _ in range(4)]

class Jogador():
    def __init__(self, nome):
        self.nome = nome
        self.palpites = []
        self.pontuacao = 0
    
    def escolhe_palpite(self):
        for i in range(4):
            posicao = int(input(f'{self.nome}, escolha uma posição de 1 a 4 para o palpite {i+1}: '))
            letra = input(f'{self.nome}, escolha a letra para o palpite {i+1} na posição {posicao}: ')
            palpite = PalpiteThread(posicao, letra)
            self.palpites.append(palpite)
        print('\n')


class PalpiteThread(threading.Thread):
    def __init__(self, posicao, letra):
        threading.Thread.__init__(self)
        self.posicao = posicao
        self.letra = letra
    
    def run(self):
        semaforo = semaforos[self.posicao-1]
        semaforo.acquire()
        print(self.posicao + ' ' + self.letra)
        semaforo.release()


jogador1 = Jogador(input('Jogador 1, digite seu nome: '))
jogador2 = Jogador(input('Jogador 2, digite seu nome: '))
jogador3 = Jogador(input('Jogador 3, digite seu nome: '))
print('-'*30 + '\n')
jogador1.escolhe_palpite()
jogador2.escolhe_palpite()
jogador3.escolhe_palpite()

# for j in range(4):
#     jogador1.palpites[j].start()
#     jogador2.palpites[j].start()
#     jogador3.palpites[j].start()


# for j in range(4):
#     jogador1.palpites[j].join()
#     jogador2.palpites[j].join()
#     jogador3.palpites[j].join()