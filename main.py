from helpers import *
from Setup import *

def play_age(table, age):
    turn = 1
    while turn < 7:
        for player in table.players:
            player.get_hand()    #get new hand
        update_cards(table)
        for player in table.players:
            player.choose()    #choose a card
            #discard last card after sixth turn
            if turn == 6:
                #if have ability to play both
                if "play2" in player.abilities:
                    player.choose()
                #special case where playing card to gain play2 ability
                elif isinstance(player.board.wonder, BabylonB) and \
                     player.board.wonderstage == 1 and \
                     player.board.buf[-1][1] == "wonder":
                    player.choose()
                else:
                    table.discard.append(player.hand[0])
                    player.hand.pop()
            #pass hand to next player
            elif age != 2:
                player.pass_hand("L")
            else:
                player.pass_hand("R")
        #take actions
        for player in table.players:
            enact(table, player)       
        #update scores and cleanup
        update_cards(table)
        for player in table.players:
            score(player)
            for resource in player.board.purchased:
                player.board.res[resource] -= 1
            player.board.lpurchased = {}
            player.board.rpurchased = {}
            player.board.purchased = []
        turn = turn + 1
        
    #determine military victory
    for player in table.players:
        victories = 0
        if player.board.milit_str > player.left.board.milit_str:
            victories += 1
        if player.board.milit_str > player.right.board.milit_str:
            victories += 1
        losses = 2 - victories
        while losses > 0:
            player.board.milit_tok.append(-1)
            losses -= 1
        while victories > 0:
            if age == 1:
                player.board.milit_tok.append(1)
            elif age == 2:
                player.board.milit_tok.append(3)
            elif age == 3:
                player.board.milit_tok.append(5)
            victories -= 1
    #update score at end of age after milit
    for player in table.players:
        score(player) 
    #guild copy ability
    for player in table.players:
        if age == 3 and "lrguildcopy" in player.abilities:
            copyable = []
            for guild in player.left.guild:
                copyable.append(guild)
            for guild in player.right.guild:
                copyable.append(guild)
            player.hand = copyable
            for card in player.hand:
                update(card, player)
            player.choose("copy")
            while player.board.actbuf:
                command = player.board.actbuf.pop()
                player.immediate_action(command)
            player.hand = []
            score(player)
                  
               

def enact(table, player):
    for command in player.board.buf:
        if isinstance(command[0], Card):
            card = command[0]
        else:
            item = command[0]
        order = command[1]

        if order == "play":
            player.board.add(card)
            player.board.money -= card.mcost
            player.board.money += card.money
            player.board.milit_str += card.stren
            #add freebuilds to list
            if card.freebuild:
                player.board.freebuilds.append(card.freebuild)
            if card.freebuild2:
                player.board.freebuilds.append(card.freebuild)
            #if static resource
            if type(card.res) == list:
                for resource in card.res:
                    player.board.res[resource] += 1
            #if split resource
            else:
                player.board.resvar.append(card.res)
            if card.ability:
                player.abilities.append(card.ability)
        elif order == "ltrade":
            cost = 2
            #determine discount
            if item == "glass" or item == "paper" or item == "cloth":
                if "reftrade" in player.abilities:
                    cost = 1
            else:
                if "ltrade" in player.abilities:
                    cost = 1
            if player.board.money >= cost:
                player.board.money -= cost
                player.board.left.money += cost
                player.board.res[item] += 1
                player.board.purchased.append(item)              
        elif order == "rtrade":
            cost = 2
            #determine discount
            if item == "glass" or item == "paper" or item == "cloth":
                if "reftrade" in player.abilities:
                    cost = 1
            else:
                if "rtrade" in player.abilities:
                    cost = 1
            if player.board.money >= cost:
                player.board.money -= cost
                player.board.right.money += cost
                player.board.res[item] += 1
                player.board.purchased.append(item)
        elif order == "discard":
            table.discard.append(card)
            player.board.money += 3
        elif order == "wonder":
            if player.board.wonder.slot1 == []:
                player.board.wonder.slot1.append(card)
                process_reward(player, player.board.wonder.r1)
            elif player.board.wonder.slot2 == []:
                player.board.wonder.slot2.append(card)
                process_reward(player, player.board.wonder.r2)
            elif player.board.wonder.slot3 == []:
                player.board.wonder.slot3.append(card)
                process_reward(player, player.board.wonder.r3)
            elif player.board.wonder.slot4 == []:
                player.board.wonder.slot4.append(card)
                process_reward(player, player.board.wonder.r4)
            player.board.wonderstage += 1
            print "wondering"
    player.board.buf = []
            
                    
def score(player):
    board = player.board
    score = 0
    #military
    for token in board.milit_tok:
        score += token
    #treasury
    score += board.money / 3
    #wonder
    score += board.wonderpoints
    #science
    score += score_science(board)
    #infrastructure
    for card in board.infra:
        player.score += card.vp
    #economy
    for card in board.econ:
        score += card.vp
    #guilds
    for card in board.guild:
        score += card.vp
    #copied cards
    for card in board.copied:
        score += card.vp
    player.score = score
    
        

if __name__ == "__main__":
    table = setup(3)
    #begin game
    age = 1
    play_age(table, age)
    age = 2
    deal(table.decks[1], table.players)
    play_age(table, age)
    age = 3
    deal(table.decks[2], table.players)
    play_age(table, age)
    #score game
    scores = []
    for player in table.players:
        scores.append(player.score)
    scores.sort()    #sort in decreasing order
    scores.reverse()
    winner = scores[0]
    print scores
    
    
        
