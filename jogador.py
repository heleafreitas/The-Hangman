# import threading

# class Jogador():
#     def __init__(self, nome):
#         self.nome = nome
#         self.palpites = []
#         self.pontuacao = 0
    
#     def escolhe_palpite(self):
#         for i in range(4):
#             posicao = int(input(f'{self.nome}, escolha uma posição de 1 a 4 para o palpite {i+1}: '))
#             letra = input(f'{self.nome}, escolha a letra para o palpite {i+1} na posição {posicao}: ')
#             palpite = PalpiteThread(posicao, letra)
#             self.palpites.append(palpite)
#             palpite.start()
#         print('\n')
#         for palpite in self.palpites:
#             palpite.join()


# class PalpiteThread(threading.Thread):
#     def __init__(self, posicao, letra):
#         threading.Thread.__init__(self)
#         self.posicao = posicao
#         self.letra = letra
    
#     def run(self):
#         semaforo = semaforos[posicao]
#         semaforo.acquire()
#         letra = input(f"Jogador {numero}, escolha uma letra para a posição {posicao}: ")
#         if letra in palavra:
#             verificar_escolha([posicao], palavra, letra)
#         else:
#             print(f"A letra {letra} não está na palavra na posição {posicao}.")
#         semaforo.release()
#         # Aqui pode ser adicionada a lógica do for original

# palpites = []
# for i in range(4):
#     posicao = int(input(f'Escolha uma posição de 1 a 4 para o palpite {i+1}: '))
#     letra = input(f'Escolha a letra para o palpite {i+1} na posição {posicao}: ')
#     palpite_thread = PalpiteThread(posicao, letra)
#     palpites.append(palpite_thread)
#     palpite_thread.start()

# for palpite_thread in palpites:
#     palpite_thread.join()
