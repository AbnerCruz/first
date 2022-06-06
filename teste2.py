import random
from re import M
import time
nrandnumb = random.randint(1,5000)
if nrandnumb < 699:
    nrandnumb = 700
style = 65
t = 2
z = ''
partycont = 1

anderson = {'nome': "Anderson",'money': random.randint(300,random.randint(round(nrandnumb/2),nrandnumb))}
flavia = {'nome': "Flávia", 'money': random.randint(300,random.randint(round(nrandnumb/2),nrandnumb))}
maria = {'nome': "Maria", 'money': random.randint(300,random.randint(round(nrandnumb/2),nrandnumb))}
gabrielly = {'nome': "Gabrielly", 'money': random.randint(300,random.randint(round(nrandnumb/4),nrandnumb))}
abner = {'nome': "Abner", 'money': random.randint(300,random.randint(round(nrandnumb/2),nrandnumb))}
joao = {'nome': "João", 'money': random.randint(300,random.randint(round(nrandnumb/2),nrandnumb))}
gabriel = {'nome': "Gabriel", 'money': random.randint(300,random.randint(round(nrandnumb/2),nrandnumb))}
andreia = {'nome': "Andréia", 'money': random.randint(300,random.randint(round(nrandnumb/2),nrandnumb))}
hitalo = {'nome': "Hítalo", 'money': random.randint(300,random.randint(round(nrandnumb/2),nrandnumb))}
kelly = {'nome': "Kelly", 'money': random.randint(300,random.randint(round(nrandnumb/2),nrandnumb))}
gustavo = {'nome': "Gustavo", 'money': random.randint(300,random.randint(round(nrandnumb/2),nrandnumb))}
bianca = {'nome': "Bianca", 'money': random.randint(300,random.randint(round(nrandnumb/2),nrandnumb))}
andre = {'nome': "André", 'money': random.randint(300,random.randint(round(nrandnumb/2),nrandnumb))}
carla = {'nome': "Carla", 'money': random.randint(300,random.randint(round(nrandnumb/2),nrandnumb))}
rogerio = {'nome': "Rogério", 'money': random.randint(300,random.randint(round(nrandnumb/2),nrandnumb))}
larissa = {'nome': "Larissa", 'money': random.randint(300,random.randint(round(nrandnumb/2),nrandnumb))}
daniel = {'nome': "Daniel", 'money': random.randint(300,random.randint(round(nrandnumb/2),nrandnumb))}
lara = {'nome': "Lara", 'money': random.randint(300,random.randint(round(nrandnumb/2),nrandnumb))}
patricia = {'nome': "Patrícia", 'money': random.randint(300,random.randint(round(nrandnumb/2),nrandnumb))}






players = []
players.append(anderson)
players.append(flavia)
players.append(maria)
players.append(gabrielly)
players.append(abner)
players.append(joao)
players.append(gabriel)
players.append(andreia)
players.append(hitalo)
players.append(kelly)
players.append(gustavo)
players.append(bianca)
players.append(andre)
players.append(carla)
players.append(rogerio)
players.append(larissa)
players.append(daniel)
players.append(lara)
players.append(patricia)

pquantity = len(players)

while True:
    p1rvalue = random.randint(0,pquantity-1)
    p2rvalue = random.randint(0,pquantity-1)
    p1 = players[p1rvalue]
    p2 = players[p2rvalue]
    if p2 == p1:
        while p2 == p1:
            p2 = players[random.randint(0,pquantity-1)]
    player1 = {'nome': p1['nome'],'points': 0, 'start': random.randint(0,100),'money': p1['money'] }
    player2 = {'nome': p2['nome'],'points': 0, 'start': random.randint(0,100),'money': p2['money'] }
    print("="*style)
    print("BIBLIOTECA")
    print("="*style)
    for i in range(0,pquantity):
        print(players[i])
    print("="*style)
    print("")
    print("")
    print("")
    print("")
    print("="*style)
    print(player1)
    print(player2)
    print("="*style)

    def spec(z):
        if z != player1["nome"] or z != player2["nome"]:
            z = ''
            z = input("Quem você acha que vai vencer? ")
            print(z)
            if z == player1 ["nome"]:
                pass
            elif z == player2["nome"]:
                pass
            else:
                while z != player1["nome"] or z != player2["nome"]:
                    print("Falha, Tente novamente", end = ' ')
                    z = input("")
                    if z == player1["nome"] or z == player2["nome"]:
                        break
                    else:
                        pass
    #spec(z)
            
        
    move = []
    cont = 0

    ret = ['.','..','...']

    def timer():
        
        for i in range(3):
            time.sleep(t)
            print(ret[i], end = '\r')
        print('\r', end = '\r')
        time.sleep(1)
        

    def bet():
        amount = random.randint(1,5+round(round(random.randint(round(round(player1["money"] + player2["money"]/random.randint(2,4))/random.randint(7,13)), round(round(player1["money"] + player2["money"]/random.randint(2,4))/random.randint(4,6))))+round(nrandnumb/round(5*random.randint(5,15)))/random.randint(1,2)))
        bet = amount*2
        return bet

    bet = bet()

    def game(move,cont,plays):
        if player1["money"] >= bet and player2["money"] >= bet:
            print('RODADA',plays)
            timer()
            print("COMECEM!")
            time.sleep(t**0)
            player1["money"] = int(player1["money"]-bet/2)
            player2["money"] = int(player2["money"]-bet/2)
            move = []
            if player1['start'] == player2 ['start']:
                while player1['start'] == player2 ['start']:
                    print("FOI IGUAL AMIGÃO")
                    player1['start'] = random.randint(0,100)
                    player2['start'] = random.randint(0,100) 
            print("")
            print("")
            print("="*style)
            print("Jogador 1:",player1["nome"] + ' [ Iniciativa:',player1["start"],']')
            print("Jogador 2:",player2["nome"]+ '[ Iniciativa:',player2["start"],']')
            print("="*style)
            print("Aposta:",bet)
            print("")
            print("")
            jogada(move,cont)
            move = []
        else:
            if player1["money"] < bet:
                print("")
                print("")
                print("="*style)
                print(player1["nome"],' não pode continuar')
                print("="*style)
                print("")
                print("")
                endgame()
            elif player2["money"] < bet:
                print("")
                print("")
                print("="*style)
                print(player2["nome"],' não pode continuar')
                print("="*style)
                print("")
                print("")
                endgame()
                

    def jogada(move,cont):
        especialcondition = 0
        #player1
        if player1['start'] > player2['start']:
            print(player1["nome"])
            for cont in range(0,3):
                timer()
                for d in range(0,3):
                    x = random.randint(1,6)
                    print("Isso aqui é o Dado",d+1,":",x)
                    move.append(x)
                    time.sleep(t**0)
                time.sleep(t)
                if move[0] == move[1] & move[1] != move[2]:
                    print(move)
                    print("tentativa:",cont+1)
                    print("Pontuação:",move[2])
                    player1['points'] = player1['points'] + move[2]
                    print("")
                    print("")
                    print("")
                    move = []
                    break
                elif move[1] == move[2] & move[2] != move[0]:
                    print(move)
                    print("tentativa:",cont+1)
                    print("Pontuação:",move[0])
                    player1['points'] = player1['points'] + move[0]
                    print("")
                    print("")
                    print("")
                    move = []
                    break
                elif move[2] == move[0] & move[0] != move[1]:
                    print(move)
                    print("tentativa:",cont+1)
                    print("Pontuação:",move[1])
                    player1['points'] = player1['points'] + move[1]
                    print("")
                    print("")
                    print("")
                    move = []
                    break
                elif move[0] == move[1] & move[1] == move[2]:
                    if move[0] == 1 | move[0] == 6:
                        print(move)
                        print("tentativa:",cont+1)
                        if move[0] == 1:
                            player1["points"] = player1["points"] + move[0]
                            player2["points"] = player2["points"] + player1["points"]
                            move = []
                            player1["money"] = player1["money"] - (bet/2)*2
                            player2["money"] = player2["money"] + (bet/2)*2
                        else:
                            move = []
                            player1["money"] = player1["money"] + (bet/2)*2
                            player2["money"] = player2["money"] - (bet/2)*2
                            especialcondition =+ 1
                            player1["points"] = player1["points"] + 1
                            player1['points'] = player1["points"] + player2["points"]
                            
                    else:
                        print(move)
                        player1['points'] = player1['points'] + move[1]
                        especialcondition = 1
                        print("tentativa",cont+1)
                        move = []
                        break
                elif move[0] == 4 & move[1] == 5 & move[2] == 6:
                    print(move)
                    print("tentativa:",cont+1)
                    player1["money"] = player1['money'] + bet/2
                    player2["money"] = player2["money"] - bet/2
                    move = []
                    player1["points"] = player1["points"] + 1
                    player1['points'] = player1["points"] + player2["points"]
                    especialcondition = 1
                    break
                elif move[0] == 1 & move[1] == 2 & move[2] == 3:
                    print(move)
                    print("tentativa:",cont+1)
                    player1["points"] = player1["points"] + 1
                    player2["points"] = player2["points"] + player1["points"]
                    move = []
                    player1["money"] = player1["money"] - bet/2
                    player2["money"] = player2["money"] + bet/2
                    break
                    
                else:
                    print('Sem nenhum ponto')
                    print(move)
                    print("tentativa:",cont+1)
                    print("")
                    print("")
                    print("")
                    move = []
                move = []
                
                
            move = []
            if especialcondition == 1:
                especialcondition = 0
                move = []
                endgame()
                
            else:
                print("")
                print("")
                print(player2["nome"])
                for cont in range(0,3):
                    timer()
                    for d in range(0,3):
                        x = random.randint(1,6)
                        print("Isso aqui é o Dado",d+1,":",x)
                        move.append(x)
                        time.sleep(t**0)
                    time.sleep(t)
                    if move[0] == move[1] & move[1] != move[2]:
                        print(move)
                        print("tentativa:",cont+1)
                        print("Pontuação:",move[2])
                        player2['points'] = player2['points'] + move[2]
                        print("")
                        print("")
                        print("")
                        move = []
                        break
                    elif move[1] == move[2] & move[2] != move[0]:
                        print(move)
                        print("tentativa:",cont+1)
                        print("Pontuação:",move[0])
                        player2['points'] = player2['points'] + move[0]
                        print("")
                        print("")
                        print("")
                        move = []
                        break
                    elif move[2] == move[0] & move[0] != move[1]:
                        print(move)
                        print("tentativa:",cont+1)
                        print("Pontuação:",move[1])
                        player2['points'] = player2['points'] + move[1]
                        print("")
                        print("")
                        print("")
                        move = []
                        break
                    elif move[0] == move[1] & move[1] == move[2]:
                        if move[0] == 1 | move[0] == 6:
                            print(move)
                            print("tentativa:",cont+1)
                            if move[0] == 1:
                                player2["points"] = player2["points"] + move[0]
                                player1["points"] = player1["points"] + player2["points"]
                                move = []
                                player2["money"] = player2["money"] - (bet/2)*2
                                player1["money"] = player1["money"] + (bet/2)*2
                            else:
                                move = []
                                player2["money"] = player2["money"] + (bet/2)*2
                                player1["money"] = player1["money"] - (bet/2)*2
                                especialcondition =+ 1
                                player2["points"] = player2["points"] + 1
                                player2['points'] = player2["points"] + player1["points"]
                            
                        else:
                            print(move)
                            player2['points'] = player2['points'] + move[1]
                            especialcondition = 1
                            print("tentativa",cont+1)
                            move = []
                            break
                    elif move[0] == 4 & move[1] == 5 & move[2] == 6:
                        print(move)
                        print("tentativa:",cont+1)
                        player2["money"] = player2['money'] + bet/2
                        player1["money"] = player1["money"] - bet/2
                        move = []
                        player2["points"] = player2["points"] + 1
                        player2['points'] = player2["points"] + player1["points"]
                        especialcondition = 1
                        break
                    elif move[0] == 1 & move[1] == 2 & move[2] == 3:
                        print(move)
                        print("tentativa:",cont+1)
                        player2["points"] = player2["points"] + 1
                        player1["points"] = player1["points"] + player2["points"]
                        move = []
                        player2["money"] = player2["money"] - bet/2
                        player1["money"] = player1["money"] + bet/2
                        break
                    
                    else:
                        print('Sem nenhum ponto')
                        print(move)
                        print("tentativa:",cont+1)
                        print("")
                        print("")
                        print("")
                        move = []
                    move = []
                move = []
                if especialcondition == 1:
                    especialcondition = 0
                    move = []
                    endgame()
                
                else:
                    move = []
                    endgame()
                
        #player2
        else:
            print(player2["nome"])
            for cont in range(0,3):
                timer()
                for d in range(0,3):
                    x = random.randint(1,6)
                    print("Isso aqui é o Dado",d+1,":",x)
                    move.append(x)
                    time.sleep(t**0)
                time.sleep(t)
                if move[0] == move[1] & move[1] != move[2]:
                    print(move)
                    print("tentativa:",cont+1)
                    print("Pontuação:",move[2])
                    player2['points'] = player2['points'] + move[2]
                    print("")
                    print("")
                    print("")
                    move = []
                    break
                elif move[1] == move[2] & move[2] != move[0]:
                    print(move)
                    print("tentativa:",cont+1)
                    print("Pontuação:",move[0])
                    player2['points'] = player2['points'] + move[0]
                    print("")
                    print("")
                    print("")
                    move = []
                    break
                elif move[2] == move[0] & move[0] != move[1]:
                    print(move)
                    print("tentativa:",cont+1)
                    print("Pontuação:",move[1])
                    player2['points'] = player2['points'] + move[1]
                    print("")
                    print("")
                    print("")
                    move = []
                    break
                elif move[0] == move[1] & move[1] == move[2]:
                    if move[0] == 1 | move[0] == 6:
                        print(move)
                        print("tentativa:",cont+1)
                        if move[0] == 1:
                            player2["points"] = player2["points"] + move[0]
                            player1["points"] = player1["points"] + player2["points"]
                            move = []
                            player2["money"] = player2["money"] - (bet/2)*2
                            player1["money"] = player1["money"] + (bet/2)*2
                        else:
                            move = []
                            player2["money"] = player2["money"] + (bet/2)*2
                            player1["money"] = player1["money"] - (bet/2)*2
                            especialcondition =+ 1
                            player2["points"] = player2["points"] + 1
                            player2['points'] = player2["points"] + player1["points"]
                            
                    else:
                        print(move)
                        player2['points'] = player2['points'] + move[1]
                        especialcondition = 1
                        print("tentativa",cont+1)
                        move = []
                        break
                elif move[0] == 4 & move[1] == 5 & move[2] == 6:
                    print(move)
                    print("tentativa:",cont+1)
                    player2["money"] = player2['money'] + bet/2
                    player1["money"] = player1["money"] - bet/2
                    move = []
                    player2["points"] = player2["points"] + 1
                    player2['points'] = player2["points"] + player1["points"]
                    especialcondition = 1
                    break
                elif move[0] == 1 & move[1] == 2 & move[2] == 3:
                    print(move)
                    print("tentativa:",cont+1)
                    player2["points"] = player2["points"] + 1
                    player1["points"] = player1["points"] + player2["points"]
                    move = []
                    player2["money"] = player2["money"] - bet/2
                    player1["money"] = player1["money"] + bet/2
                    break
                    
                else:
                    print('Sem nenhum ponto')
                    print(move)
                    print("tentativa:",cont+1)
                    print("")
                    print("")
                    print("")
                    move = []
                move = []
            move = []
            if especialcondition == 1:
                especialcondition = 0
                move = []
                endgame()
                
            else:
                print("")
                print("")
                print(player1["nome"])
                for cont in range(0,3):
                    timer()
                    for d in range(0,3):    
                        x = random.randint(1,6)
                        print("Isso aqui é o Dado",d+1,":",x)
                        move.append(x)
                        time.sleep(t**0)
                    time.sleep(t)
                    if move[0] == move[1] & move[1] != move[2]:
                        print(move)
                        print("tentativa:",cont+1)
                        print("Pontuação:",move[2])
                        player1['points'] = player1['points'] + move[2]
                        print("")
                        print("")
                        print("")
                        move = []
                        break
                    elif move[1] == move[2] & move[2] != move[0]:
                        print(move)
                        print("tentativa:",cont+1)
                        print("Pontuação:",move[0])
                        player1['points'] = player1['points'] + move[0]
                        print("")
                        print("")
                        print("")
                        move = []
                        break
                    elif move[2] == move[0] & move[0] != move[1]:
                        print(move)
                        print("tentativa:",cont+1)
                        print("Pontuação:",move[1])
                        player1['points'] = player1['points'] + move[1]
                        print("")
                        print("")
                        print("")
                        move = []
                        break
                    elif move[0] == move[1] & move[1] == move[2]:
                        if move[0] == 1 | move[0] == 6:
                            print(move)
                            print("tentativa:",cont+1)
                            if move[0] == 1:
                                player1["points"] = player1["points"] + move[0]
                                player2["points"] = player2["points"] + player1["points"]
                                move = []
                                player1["money"] = player1["money"] - (bet/2)*2
                                player2["money"] = player2["money"] + (bet/2)*2
                            else:
                                move = []
                                player1["money"] = player1["money"] + (bet/2)*2
                                player2["money"] = player2["money"] - (bet/2)*2
                                especialcondition =+ 1
                                player1["points"] = player1["points"] + 1
                                player1['points'] = player1["points"] + player2["points"]
                            
                        else:
                            print(move)
                            player1['points'] = player1['points'] + move[1]
                            especialcondition = 1
                            print("tentativa",cont+1)
                            move = []
                            break
                    elif move[0] == 4 & move[1] == 5 & move[2] == 6:
                        print(move)
                        print("tentativa:",cont+1)
                        player1["money"] = player1['money'] + bet/2
                        player2["money"] = player2["money"] - bet/2
                        move = []
                        player1["points"] = player1["points"] + 1
                        player1['points'] = player1["points"] + player2["points"]
                        especialcondition = 1
                        break
                    elif move[0] == 1 & move[1] == 2 & move[2] == 3:
                        print(move)
                        print("tentativa:",cont+1)
                        player1["points"] = player1["points"] + 1
                        player2["points"] = player2["points"] + player1["points"]
                        move = []
                        player1["money"] = player1["money"] - bet/2
                        player2["money"] = player2["money"] + bet/2
                        break
                    
                    else:
                        print('Sem nenhum ponto')
                        print(move)
                        print("tentativa:",cont+1)
                        print("")
                        print("")
                        print("")
                        move = []
                    move = []
                move = []
                if especialcondition == 1:
                    especialcondition = 0
                    move = []
                    endgame()
                
                else:
                    move = []
                    endgame()
            
    def winner(move,cont):
        if player1["points"] == player2["points"]:
            if player1["money"] >= bet and player2["money"] >= bet:
                print("")
                print("="*style)
                print("Desempate")
                print("="*style)
                print("")
                jogada(move,cont)
            else:
                if player1["money"] < bet:
                    print("")
                    print("")
                    print("="*style)
                    print(player1["nome"],' não pode continuar')
                    print("="*style)
                    print("")
                    print("")
                elif player2["money"] < bet:
                    print("")
                    print("")
                    print("="*style)
                    print(player2["nome"],' não pode continuar')
                    print("="*style)
                    print("")
                    print("")
        else:
            if player1["points"] > player2["points"]:
                print("")
                print(player1["nome"]," é o vencedor!")
                print("")
                player1["money"] = player1["money"] + bet
                print("")
                print("")
                print("="*style)
                print("Jogador 1",player1)
                print("Jogador 2",player2)
                print("="*style)
                print("")
                print("")
            else:
                print("")
                print(player2["nome"]," é o vencedor!")
                print("")
                player2["money"] = player2["money"] + bet
                print("")
                print("")
                print("="*style)
                print("Jogador 1",player1)
                print("Jogador 2",player2)
                print("="*style)
                print("")
                print("")
        
    def endgame():
        print("")
        print("")
        print("="*style)
        print("FIM DE JOGO")
        print("Jogador 1 pontuação:",player1["points"]) 
        print("Jogador 2 pontuação:",player2["points"])
        print("="*style)
        print("")
        print("")
        move = []
        winner(move,cont)

    for i in range(0,1):
        print("JOGO NUMERO:",i+1)
        print("Aposta:",bet)
        for i in range(0,3):
            game(move,cont,i+1)
        p1["money"] = player1["money"]
        p2["money"] = player2["money"]
    print("")
    print("="*style)
    print("Encerrando Partida n°",partycont)
    print("="*style)
    print("")
    timer()
    partycont += 1