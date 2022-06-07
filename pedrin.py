import random
anderson = {'nome': "Anderson",'money': 200000000000}
flavia = {'nome': "Flávia", 'money': 200}
maria = {'nome': "Maria", 'money': 200}
gabrielly = {'nome': "Gabrielly", 'money': 200}
abner = {'nome': "Abner", 'money': 200}
joao = {'nome': "João", 'money': 200}

players = []
players.append(anderson)
players.append(flavia)
players.append(maria)
players.append(gabrielly)
players.append(abner)
players.append(joao)


p1 = players[random.randint(0,len(players))]
p2 = players[random.randint(0,len(players))]
if p2 == p1:
    while p2 == p1:
        p2 = players[random.randint(0,len(players))]
player1 = {'nome': p1['nome'],'points': 0, 'start': random.randint(0,100),'money': p1['money'] }
player2 = {'nome': p2['nome'],'points': 0, 'start': random.randint(0,100),'money': p2['money'] }
print(player1)
print(player2)
z = input("Qual jogador irá vencer?")
move = []
cont = 0



def bet():
    amount = random.randint(1,100)
    bet = amount*2
    return bet

bet = bet()

def game(move,cont,plays):
    print('RODADA',plays)
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
    print("Jogador 1:",player1)
    print("Jogador 2:",player2)
    print("Aposta:",bet)
    print("")
    print("")
    jogada(move,cont)
    move = []

def jogada(move,cont):
    especialcondition = 0
    #player1
    if player1['start'] > player2['start']:
        print("JOGADOR 1")
        for cont in range(0,3):
            for d in range(0,3):
                x = random.randint(1,6)
                print("Isso aqui é o Dado",d+1,":",x)
                move.append(x)
            
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
            print('JOGADOR 2')
            for cont in range(0,3):
                for d in range(0,3):
                    x = random.randint(1,6)
                    print("Isso aqui é o Dado",d+1,":",x)
                    move.append(x)
            
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
        print("JOGADOR 2")
        for cont in range(0,3):
            for d in range(0,3):
                x = random.randint(1,6)
                print("Isso aqui é o Dado",d+1,":",x)
                move.append(x)
            
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
            print('JOGADOR 1')
            for cont in range(0,3):
                for d in range(0,3):
                    x = random.randint(1,6)
                    print("Isso aqui é o Dado",d+1,":",x)
                    move.append(x)
            
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
        print("")
        print("")
        print("Desempate")
        print("")
        print("")
        jogada(move,cont)
    else:
        if player1["points"] > player2["points"]:
            print("")
            print("Jogador 1 é o vencedor!")
            print("")
            player1["money"] = player1["money"] + bet
            print("")
            print("")
            print("Jogador 1",player1)
            print("Jogador 2",player2)
            print("")
            print("")
        else:
            print("")
            print('Jogador 2 é o vencedor!')
            print("")
            player2["money"] = player2["money"] + bet
            print("")
            print("")
            print("Jogador 1",player1)
            print("Jogador 2",player2)
            print("")
            print("")
    
def endgame():
    print("")
    print("")
    print("")
    print("FIM DE JOGO")
    print("Jogador 1 pontuação:",player1["points"]) 
    print("Jogador 2 pontuação:",player2["points"])
    print("")
    print("")
    print("")
    move = []
    winner(move,cont)

for i in range(0,3):
    print("JOGO NUMERO:",i+1)
    for i in range(0,3):
        game(move,cont,i+1)