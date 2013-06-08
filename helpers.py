from PlayerClass import *


def update_cards(table):
    '''update all cards that need updates'''
    for player in table.players:
        #update hands
        if player.hand:
            for card in player.hand:
                update(card, player)
        #update cards on board
        for card in player.board.guild:
            update(card, player)
        for card in player.board.econ:
            update(card, player)
        for card in player.board.copied:
            update(card, player)

def update(c, player):
    '''update vp or money value of a card in the hand of player'''
    if c.update:
        for update in c.update:
            direc = update[0]   #which direction
            utype = update[1]   #update what value
            param = update[2]   #what is being counted
            val = update[3]    #vp for each counted item
        
        if utype == "vp":
            c.vp = direct(player, direc, param, val)
        if utype == "money":
            c.money = direct(player, direc, param, val)
        

def direct(player, direc, param, val):
    if direc == "lrs":
        return (count(player.left, param) + count(player.right, param)
        + count(player, param)) * val
    elif direc == "lr":
        return (count(player.left, param) + count(player.right, param)) * val
    elif direc == "s":
        return count(player, param) * val    

def count(player, param):
    '''count the number of param on board of player'''
    if param == "brown":
        return len(player.board.resraw)
    elif param == "grey":
        return len(player.board.resref)
    elif param == "yellow":
        return len(player.board.econ)
    elif param == "green":
        return len(player.board.science)
    elif param == "red":
        return len(player.board.military)
    elif param == "blue":
        return len(player.board.infra)
    elif param == "brown/grey/purple":
        return len(player.board.resraw) + len(player.board.resref) + len(player.board.guild)
    elif param == "wonder":
        return player.board.wonderstage
    elif param == "loss":
        i = 0
        for token in player.board.milit_tok:
            if token == -1:
                i = i + 1
        return i
    

def score_science(board):
    if board.wildsci > 0:
        scores = []
        wildcombos = itertools.combinations_with_replacement\
            (["gear", "tablet", "compass"], board.wildsci)
        for combo in wildcombos:
            nc = board.compass
            ng = board.gear
            nt = board.tablet            
            for symbol in combo:
                if symbol == "compass":
                    nc += 1
                elif symbol == "gear":
                    ng += 1
                elif symbol == "tablet":
                    nt += 1
            scores.append(science_calc(nc, ng, nt))
        return max(scores)
    else:
        return science_calc(board.compass, board.gear, board.tablet)
                
    
def science_calc(compass, gear, tablet):
    score = 0
    score += compass ** 2
    score += gear ** 2
    score += tablet ** 2
    score += 7 * min(compass, gear, tablet)
    return score

def process_reward(player, rewards):
    '''give Player player the rewards in list rewards'''
    for reward in rewards:
        rdetail = reward[0]
        rtype = reward[1]
        if rtype == "vp":
            player.board.wonderpoints += rdetail
        elif rtype == "money":
            player.board.money += rdetail
        elif rtype == "res":
            player.board.res[rdetail] += 1
        elif rtype == "mil":
            player.board.mil_str += rdetail
        elif rtype == "sci":
            if rdetail == "wild":
                player.board.wildsci += 1