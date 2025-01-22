from random import randint

lista_npcs = []

players = []

def define_classe():
    resp = 1
    while(resp > 4 or resp < 0):
        print("====================")
        print("=  [1] - Mago      =")
        print("=  [2] - Cavaleiro =")
        print("=  [3] - Arqueiro  =")
        print("=  [4] - Tank      =")
        print("=  [0] - Sair      =")
        print("====================")
        resp = int(print("=> "))
        return resp

def criar_player():
    nomee = input("Insira o nome do player: ")
    classe = define_classe()

    poder_magico = 0
    dano_fisico = 0
    defesa = 0
    hp = 0
    if (classe == "mago"):
        poder_magico = 600
        dano_fisico = 20
        defesa = 100
    elif(classe == "cavaleiro"):
        poder_magico = 10
        dano_fisico = 450
        defesa = 300
    elif(classe == "arqueiro"):
        poder_magico = 230
        dano_fisico = 300
        defesa = 200
    else:
        poder_magico = 50
        dano_fisico = 250
        defesa = 500
    
    player_criado = {
        "nome": f"{nomee}",
        "level": 1,
        "classe": f"{classe}"
    }

    return player_criado

def gerar_players(n_players):
    for x in range(n_players):
        player_criado = criar_player()
        players.append(player_criado)

def exibir_player():
    for player in players:
        print(f"Nome: {player['nome']} // Level: {player['level']} // Classe: {player['classe']}")

def criar_monstro():
    level = randint(1,50)

    novo_npc = {
        "nome": f"Monstro #{level}",
        "level": level,
        "dano": 5 * level,
        "hp": 100 * level
    }

    return novo_npc

def gerar_monstros(n_npcs):
    for x in range(n_npcs):
        novo_npc = criar_monstro()
        lista_npcs.append(novo_npc)

def exibir_monstros():
    for npc in lista_npcs:
        print(f"Nome: {npc['nome']} // Level: {npc['level']} // {npc['dano']} // Hp: {npc['hp']}")

number = int(input("Deseja criar quantos monstros? "))

gerar_monstros(number)

exibir_monstros()

players_quantity = int(input("Deseja criar quantos players? "))


gerar_players(players_quantity)

exibir_player()