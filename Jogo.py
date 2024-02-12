import random

class Personagem:
    def __init__(self, nome, vida, nivel):
       self.__nome = nome
       self.__vida = vida
       self.__nivel = nivel

    def get_nome(self):
        return self.__nome
    def get_vida(self):
        return self.__vida
    def get_nivel(self):
        return self.__nivel
    def exibir_detalhes(self):
        return f'Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNivel: {self.get_nivel()}'
    
    def receber_ataque(self, dano):
            self.__vida -= int(dano)
            if self.__vida < 0:
                self.__vida = 0

    def atacar(self, alvo):
        dano = random.randint(self.get_nivel()* 2, self.get_nivel() *4) # Basado no nivel
        alvo.receber_ataque(dano)
        print(f'{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!')

class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade
    def get_habilidade(self):
        return self.__habilidade
    def exibir_detalhes(self):
        return f'{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}\n'
    def ataque_especial(self, alvo):
        dano = random.randint(self.get_nivel()* 5, self.get_nivel() *8)                 #Dano aumentado
        alvo.receber_ataque(dano)
        print(f'Usou habilidade especial {self.get_habilidade()} em {alvo.get_nome()} e causou {dano} de dano!')
    
class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo
    def get_tipo(self):
        return self.__tipo  
    def exibir_detalhes(self):
        return f'{super().exibir_detalhes()}\nTipo: {self.get_tipo()}\n'
    
class Jogo:
    ''' Classe orquestradora do jogo'''

    def __init__(self) -> None:
        self.heroi = Heroi(nome= 'Herói', vida= 100, nivel=5, habilidade='Super Forçar')
        self.inimigo = Inimigo(nome='Morcego', vida=50, nivel=3, tipo='Voador')
        #Criando um novo inimigo para testar
        self.inimigo = Inimigo(nome='Morcego', vida=80, nivel=5, tipo='Voador')
    def iniciar_batalha(self):
        ''' Fazer a gestao da batalha em turnos'''
        print('Iniciada batalha')
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print('\nDetalhes dos Personagens:')
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())
            '''Ataque do Heroi'''
            input('Precione Enter para atacar...')
            escolha =  input('Escolha (1 - Ataque Normal, 2 - Ataque Especial): ')
                        
            
            if escolha == '1':
                self.heroi.atacar(self.inimigo)
            elif escolha == '2':
                self.heroi.ataque_especial(self.inimigo)
            else:
                print('Escolha invalida. Escolha novamente.')
            '''Ataque inimigo'''
            if self.inimigo.get_vida() > 0:
                self.inimigo.atacar(self.heroi)
                
            
            

        if self.heroi.get_vida()> 0:
            print('Parabéns, você venceu!')
        else:
            print('Você foi derrotado!')

            ''' 
            else:
                while escolha > 0 and escolha < 3:
                    print('Escolha 1 ou 2')
                    escolha =  input(int('Escolha (1 - Ataque Normal, 2 - Ataque Especial): '))
                    if escolha == 1:
                        self.inimigo.get_vida -= dano
                    elif escolha == 2:
                        dano = dano*1,3
                        self.inimigo.get_vida -= dano
            '''

# Criar instacia do jogo e iniciar batalha
jogo = Jogo()
jogo.iniciar_batalha()

'''
    heroi = Heroi(nome= 'Herói', vida= 100, nivel=5, habilidade='Super Forçar')
    print(heroi.exibir_detalhes())
    Inimigo = Inimigo(nome='Morcego', vida=50, nivel=3, tipo='Voador')
    print(Inimigo.exibir_detalhes())
'''