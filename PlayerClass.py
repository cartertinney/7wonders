import random
import copy
import itertools
from boardClass import *
from HandCardClasses import *

class Player:
    def __init__(self, ai_type):
        self.hand = []
        self.handbuf = []    #incoming hand buffer
        self.board = Board()
        self.abilities = []   #the abilities the player has (i.e. reduced trade)
        self.ai = ai_type    #the name of the AI
        self.score = 0
        
        self.left = None
        self.right = None
    

    def immediate_action(self, command):
        card = command[0]
        order = command[1]
        if order == "copy":
            player.board.copied.append(card)
            player.board.money += card.money
            player.board.milit_str += card.stren
            if card.ability:
                player.abilities.append(card.ability)            
            #copy science symbol
            if card.symbol == "wild":
                player.board.wildsci += 1
            elif card.symbol == "gear":
                player.board.gear += 1
            elif card.symbol == "compass":
                player.board.compass += 1
            elif card.symbol == "tablet":
                player.board.tablet += 1 
        
        
    def choose(self, typ="normal"):
        '''choose a card from hand with ai
        typ = "normal" -> play card, must pay cost
        typ = "free" -> play card, free
        typ = "copy" -> copy card, free
        '''
        r = random.randint(0, len(self.hand) - 1)
        card = self.hand[r]
        #send hand and typ to ai
        if typ == "normal":
            self.play(card)
        elif typ == "free":
            self.play(card, True)
        elif typ == "copy":
            self.actbuf.append((card, "copy"))
            
        #s = random.randint(0, 2)
        #if s == 1 or s == 2:
            #self.play(card)
        #if s == 0:
            #self.wonder(card)
    
    def get_hand(self):
        '''recieve a Hand h from buffer'''
        self.hand = self.handbuf
    
    def pass_hand(self, direc):
        '''pass Hand in a direction direc'''
        if direc == "L":
            self.left.handbuf = self.hand
            self.hand = None
        elif direc == "R":
            self.right.handbuf = self.hand
            self.hand = None
        
          
    def play(self, c, free=False):
        '''play Card c from hand to board'''
        #check to see if have required resources
        valid = False
        if self.check_validity(c) and (free or self.check_resources(c) == []):
            valid = True
        self.hand.remove(c)
        if valid:
            self.board.buf.append((c, "play"))
            print (self.ai, c, "play")
        else:
            self.board.buf.append((c, "discard"))
            print (self.ai, c, "discard")
        
    def discard(self, c):
        '''play Card c from hand to discard pile'''
        self.hand.remove(c)
        self.board.buf.append((c, "discard"))
        
    def wonder(self, c):
        '''play Card c from hand as a wonder'''
        valid = False
        if self.check_validity(self.board.wonder) and \
           self.check_resources(self.board.wonder) == []:
            valid = True
        self.hand.remove(c)
        if valid:
            self.board.buf.append((c, "wonder"))
        else:
            self.board.buf.append((c, "discard"))
     

    def purchase_resource(self, direc, res):
        '''purchase resource res from player in direc (l or r)'''
        valid = False
        if direc == "l":
            if res == "wood" or res == "ore" or res == "brick" or res == "stone":
                for card in self.left.board.resraw:
                    for resource in card.res:
                        if resource == res:
                            #if card has not already been purchased from
                            if card not in self.board.lpurchased:
                                valid = True
                                self.board.lpurchased[card] = 1
                                self.board.buf.append((res, "ltrade"))
                            #if card has been purchased from
                            else:
                                #if card can still be purchased from
                                if len(card.res) > self.board.lpurchased[card]\
                                   and type(card.res) != tuple:
                                    valid = True
                                    self.board.lpurchased[card] += 1
                                    self.board.buf.append((res, "ltrade"))
            elif res == "glass" or res == "paper" or res == "cloth":
                for card in self.left.board.resref:
                    for resource in card.res:
                        if resource == res:
                            #if card has not already been purchased from
                            if card not in self.board.lpurchased:
                                valid = True
                                self.board.lpurchased[card] = 1
                                self.board.buf.append((res, "ltrade"))
                            #if card has been purchased from
                            else:
                                #if card can still be purchased from
                                if len(card.res) > self.board.lpurchased[card]\
                                   and type(card.res) != tuple:
                                    valid = True
                                    self.board.lpurchased[card] += 1
                                    self.board.buf.append((res, "ltrade"))       
        elif direc == "r":
            if res == "wood" or res == "ore" or res == "brick" or res == "stone":
                for card in self.right.board.resraw:
                    for resource in card.res:
                        if resource == res:
                            #if card has not already been purchased from
                            if card not in self.board.rpurchased:
                                valid = True
                                self.board.rpurchased[card] = 1
                                self.board.buf.append((res, "rtrade"))
                            #if card has been purchased from
                            else:
                                #if card can still be purchased from
                                if len(card.res) > self.board.rpurchased[card]\
                                   and type(card.res) != tuple:
                                    valid = True
                                    self.board.rpurchased[card] += 1
                                    self.board.buf.append((res, "rtrade"))
            elif res == "glass" or res == "paper" or res == "cloth":
                for card in self.right.board.resref:
                    for resource in card.res:
                        if resource == res:
                            #if card has not already been purchased from
                            if card not in self.board.rpurchased:
                                valid = True
                                self.board.rpurchased[card] = 1
                                self.board.buf.append((res, "rtrade"))
                            #if card has been purchased from
                            else:
                                #if card can still be purchased from
                                if len(card.res) > self.board.rpurchased[card]\
                                   and type(card.res) != tuple:
                                    valid = True
                                    self.board.rpurchased[card] += 1
                                    self.board.buf.append((res, "rtrade"))

    def check_validity(self, c):
        '''determine if valid to play Card c or build Wonder c. Return bool t/f'''
        if isinstance(c, Card):
            #check monetary cost
            if c.mcost > self.board.money:
                return False
            #check if card has already been played
            if c.colour == "blue":
                return c not in self.board.infra
            if c.colour == "red":
                return c not in self.board.military
            elif c.colour == "green":
                return c not in self.board.science
            elif c.colour == "yellow":
                return c not in self.board.econ
            elif c.colour == "purple":
                return c not in self.board.guild
            elif c.colour == "brown":
                return c not in self.board.resraw
            elif c.colour == "grey":
                return c not in self.board.resref
        else:
        #wonder
            if c.slot1 == []:
                return True
            elif c.slot2 == []:
                return True
            elif c.slot3 == []:
                return True
            elif c.slot4 == []:
                return True
            else:
                return False
        
    def check_resources(self, c):
        '''determine the resouces still needed to play Card or Wonder c.
        Returns a list of lists, each representing a different set of resources
        that may be needed. Satisfying any of these lists will allow play of card'''
        if isinstance(c, Card):
            req = c.rescost
            if c.name in self.board.freebuilds:
                return []
        else:
            if c.slot1 == []:
                req = c.cost1
            elif c.slot2 == []:
                req = c.cost2
            elif c.slot3 == []:
                req = c.cost3
            elif c.slot4 == []:
                req = c.cost4
            else:
                #can be assured will not reach here due to validity check
                pass
        missing = []
        resdict = copy.copy(self.board.res)
        split = copy.copy(self.board.resvar)
        #first check the static resources in the dict
        for res in req:
            if resdict[res] > 0:
                resdict[res] -= 1
            else:
                missing.append(res)
        if missing == [] or not split:
            return missing
        elif split:
            #if missing res create all possible combos of split resources
            combinations = _rescombos(split)
            master = []
            for combo in combinations:
                remaining = copy.copy(missing)
                for resource in combo:
                    if resource in remaining:
                        remaining.remove(resource)
                master.append(remaining)
            #at this point master is now left with all possible combos of needed
            #resources prior to implementation of wilds
            if [] in master:
                return []
            elif [] not in master:
                wildraws = resdict["wildraw"]
                wildrefs = resdict["wildref"]
                #if there are no wildcards
                if not wildraws and not wildrefs:
                    return master
                else:
                    final = []
                    rawtypes = ["ore", "stone", "brick", "wood"]
                    reftypes = ["paper", "cloth", "glass"]
                    master_raw = []
                    master_ref = []
                    #create two paired lists of different res types (same indicies)
                    for combo in master:
                        raws = []
                        refs = []
                        for resource in combo:
                            #if resource is raw
                            if resource in rawtypes:
                                raws.append(resource)
                            else:
                                refs.append(resource)
                        master_raw.append(raws)
                        master_ref.append(refs)
                    for i in range(0, len(master_raw)):   #master_raw and master_ref are same size
                        rawdif = len(master_raw[i]) - wildraws
                        if rawdif > 0:
                            rawcombos = list(itertools.combinations(master_raw[i], rawdif))
                        else:
                            rawcombos = [()]   #list of tuples of combinations
                        refdif = len(master_ref[i]) - wildrefs
                        if refdif > 0:
                            refcombos = list(itertools.combinations(master_ref[i], refdif))
                        else:
                            refcombos = [()]
                        #combine all possible combos
                        for raw_tup in rawcombos:
                            a = list(raw_tup)
                            for ref_tup in refcombos:
                                b = list(ref_tup)
                                c = a + b
                                if c not in final:
                                    final.append(c)
                    return final
                
        
def _rescombos(arr, idx=0):
    '''generate all possible combos of the split resources in arr'''
    if idx == len(arr) -1:
        return [[arr[idx][0]], [arr[idx][1]]]
    else:
        next_vals = _rescombos(arr, idx + 1)
        master = []
        for combo in next_vals:
            comboA = [arr[idx][0]]
            comboB = [arr[idx][1]]
            for item in combo:
                comboA.append(item)
                comboB.append(item)
            master.append(comboA)
            master.append(comboB)
        return master
                    
                    
                    
                
            
            
            


if __name__ == "__main__":
    p = Player(1)
    p.board.resvar = [("wood", "stone")]
    p.board.res["wildraw"] = 2
    p.board.res["wildref"] = 1
    print p.check_resources(Pantheon())