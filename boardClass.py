#class Discard():
    #def __init__(self):
        #self.pile = []
        
    #def add(c):
        #'''add Card c to discard pile'''
        #self.pile.append(c)
    
    #def remove(c):
        #'''remove Card c from discard pile'''
        #self.pile.remove(c)
        
        
class Table():
    def __init__(self):
        self.players = []
        self.boards = []    #all boards. idx 0 = player 1
        self.discard = []    #tablewide discard
        self.decks = []
        

class Board():
    
    def __init__(self):
        self.wonder = None
        self.science = []    #list of science cards
        self.econ = []    #list of economy cards
        self.guild = []    #list of guild cards
        self.infra = []    #list of infrastructure cards
        self.resraw = []    #list of raw resource cards
        self.resref = []    #list of refinedresource cards
        self.military = []    #list of military cards
        self.copied = []    #list of copied cards
        #dictionary mapping resource name to number available
        self.res = {"wood" : 0, "stone" : 0, "brick" : 0, "ore" : 0, \
                    "glass" : 0, "paper" : 0, "cloth" : 0, \
                    "wildraw" : 0, "wildref" : 0}    
        self.resvar = []    #list of variable resources (e.g. wood/ore)
                            #(tuples containing the two resources)
        self.freebuilds = []    #list of cards that can be built for free w/ chain
        self.buf = []   #list of buffers for playing card (card, action)
        self.actbuf = [] #buffer for list of immeidate actions
        self.money = 3
        self.milit_str = 0
        self.wonderpoints = 0    #number of points given by completed wonder stages
        self.wonderstage = 0    #number of stages complete
        self.milit_tok = []   #military victory pieces
        
        #science symbol counts
        self.compass = 0
        self.gear = 0
        self.tablet = 0
        self.wildsci = 0
        
        self.lpurchased = {} #cards purchased from left and right players
        self.rpurchased = {}   #card : num res purchased from it
        self.purchased = [] #list of resources purchased on turn
        
        self.left = None    #board to left
        self.right = None    #board to right
        self.others = []    #other boards (left to right)
        
        
    def add(self, card):
        if card.colour == "green":
            self.science.append(card)
            if card.symbol == "compass":
                self.compass += 1
            elif card.symbol == "gear":
                self.gear += 1
            elif card.symbol == "tablet":
                self.tablet += 1
        elif card.colour == "red":
            self.military.append(card)
        elif card.colour == "yellow":
            self.econ.append(card)
        elif card.colour == "purple":
            self.guild.append(card)
            if card.symbol == "wild":
                self.wildsci += 1
        elif card.colour == "blue":
            self.infra.append(card)
        elif card.colour == "brown":
            self.resraw.append(card)
        elif card.colour == "grey":
            self.resref.append(card)
    
        
    def get_wonder(wonder):
        self.wonder = wonder
        
    def update_discard(board,):
        self.discard = discard
        

class Wonder():
    
    def __init__(self):
        self.name = ""
        self.resource = None
        self.slot1 = None
        self.slot2 = None
        self.slot3 = None
        self.slot4 = None
        self.cost1 = None
        self.cost2 = None
        self.cost3 = None
        self.cost4 = None
        self.r1 = []    #reward. Tuples with (#, type), or str ability name
        self.r2 = [] 
        self.r3 = []
        self.r4 = []

class RhodosA(Wonder):
    def __init__(self):
        Wonder.__init__(self)
        self.resource = "ore"
        self.slot1 = []
        self.slot2 = []
        self.slot3 = []
        self.cost1 = ["wood", "wood"]
        self.cost2 = ["brick", "brick", "brick"]
        self.cost3 = ["ore", "ore", "ore", "ore"]
        self.r1 = [(3, "vp")]
        self.r2 = [(2, "mil")]
        self.r3 = [(7, "vp")]
        
class AlexandriaA(Wonder):
    def __init__(self):
        Wonder.__init__(self)
        self.resource = "glass"
        self.slot1 = []
        self.slot2 = []
        self.slot3 = []
        self.cost1 = ["stone", "stone"]
        self.cost2 = ["ore", "ore"]
        self.cost3 = ["glass", "glass"]
        self.r1 = [(3, "vp")]
        self.r2 = [("wildraw", "res")]
        self.r3 = [(7, "vp")]
        
class EphesosA(Wonder):
    def __init__(self):
        Wonder.__init__(self)
        self.resource = "paper"
        self.slot1 = []
        self.slot2 = []
        self.slot3 = []
        self.cost1 = ["stone", "stone"]
        self.cost2 = ["wood", "wood"]
        self.cost3 = ["paper", "paper"]
        self.r1 = [(3, "vp")]
        self.r2 = [(9, "money")]
        self.r3 = [(7, "vp")]
        
class BabylonA(Wonder):
    def __init__(self):
        Wonder.__init__(self)
        self.resource = "brick"
        self.slot1 = []
        self.slot2 = []
        self.slot3 = []
        self.cost1 = ["brick", "brick"]
        self.cost2 = ["wood", "wood", "wood"]
        self.cost3 = ["brick", "brick", "brick", "brick"]
        self.r1 = [(3, "vp")]
        self.r2 = [("wild", "sci")]
        self.r3 = [(7, "vp")]

class OlympiaA(Wonder):
    def __init__(self):
        Wonder.__init__(self)
        self.resource = "wood"
        self.slot1 = []
        self.slot2 = []
        self.slot3 = []
        self.cost1 = ["wood", "wood"]
        self.cost2 = ["stone", "stone"]
        self.cost3 = ["ore", "ore"]
        self.r1 = [(3, "vp")]
        self.r2 = [("freebuild", "ability")]
        self.r3 = [(7, "vp")]

class HalikarnassosA(Wonder):
    def __init__(self):
        Wonder.__init__(self)
        self.resource = "cloth"
        self.slot1 = []
        self.slot2 = []
        self.slot3 = []
        self.cost1 = ["brick", "brick"]
        self.cost2 = ["ore", "ore", "ore"]
        self.cost3 = ["cloth", "cloth"]
        self.r1 = [(3, "vp")]
        self.r2 = [("discardbuild", "action")]
        self.r3 = [(7, "vp")]
        
class GizahA(Wonder):
    def __init__(self):
        Wonder.__init__(self)
        self.resource = "stone"
        self.slot1 = []
        self.slot2 = []
        self.slot3 = []
        self.cost1 = ["stone", "stone"]
        self.cost2 = ["wood", "wood", "wood"]
        self.cost3 = ["stone", "stone", "stone", "stone"]
        self.r1 = [(3, "vp")]
        self.r2 = [(5, "vp")]
        self.r3 = [(7, "vp")]
        
class RhodosB(Wonder):
    def __init__(self):
        Wonder.__init__(self)
        self.resource = "ore"
        self.slot1 = []
        self.slot2 = []
        self.cost1 = ["stone", "stone", "stone"]
        self.cost2 = ["ore", "ore", "ore", "ore"]
        self.r1 = [(1, "mil"), (3, "vp"), (3, "money")]
        self.r2 = [(1, "mil"), (4, "vp"), (4, "money")]
        
class AlexandriaB(Wonder):
    def __init__(self):
        Wonder.__init__(self)
        self.resource = "glass"
        self.slot1 = []
        self.slot2 = []
        self.slot3 = []
        self.cost1 = ["brick", "brick"]
        self.cost2 = ["wood", "wood"]
        self.cost3 = ["stone", "stone", "stone"]
        self.r1 = [("wildraw", "res")]
        self.r2 = [("wildref", "res")]
        self.r3 = [(7, "vp")]
        
class EphesosB(Wonder):
    def __init__(self):
        Wonder.__init__(self)
        self.resource = "paper"
        self.slot1 = []
        self.slot2 = []
        self.slot3 = []
        self.cost1 = ["stone", "stone"]
        self.cost2 = ["wood", "wood"]
        self.cost3 = ["paper", "cloth", "glass"]
        self.r1 = [(2, "vp"), (4, "money")]
        self.r2 = [(3, "vp"), (4, "money")]
        self.r3 = [(5, "vp"), (4, "money")]
        
class BabylonB(Wonder):
    def __init__(self):
        Wonder.__init__(self)
        self.resource = "brick"
        self.slot1 = []
        self.slot2 = []
        self.slot3 = []
        self.cost1 = ["cloth", "brick"]
        self.cost2 = ["glass", "wood", "wood"]
        self.cost3 = ["brick", "brick", "brick", "paper"]
        self.r1 = [(3, "vp")]
        self.r2 = [("play2", "ability")]
        self.r3 = [("wild", "sci")]

class OlympiaB(Wonder):
    def __init__(self):
        Wonder.__init__(self)
        self.resource = "wood"
        self.slot1 = []
        self.slot2 = []
        self.slot3 = []
        self.cost1 = ["wood", "wood"]
        self.cost2 = ["stone", "stone"]
        self.cost3 = ["cloth", "ore", "ore"]
        self.r1 = [("ltrade", "ability"), ("rtrade", "ability")]
        self.r2 = [(5, "vp")]
        self.r3 = [("lrguildcopy", "ability")]
        
class HalikarnassosB(Wonder):
    def __init__(self):
        Wonder.__init__(self)
        self.resource = "cloth"
        self.slot1 = []
        self.slot2 = []
        self.slot3 = []
        self.cost1 = ["ore", "ore"]
        self.cost2 = ["brick", "brick", "brick"]
        self.cost3 = ["glass", "paper", "cloth"]
        self.r1 = [(2, "vp"), ("discardbuild", "action")]
        self.r2 = [(1, "vp"), ("discardbuild", "action")]
        self.r3 = [("discardbuild", "action")]
        
class GizahB(Wonder):
    def __init__(self):
        Wonder.__init__(self)
        self.resource = "stone"
        self.slot1 = []
        self.slot2 = []
        self.slot3 = []
        self.slot4 = []
        self.cost1 = ["wood", "wood"]
        self.cost2 = ["stone", "stone", "stone"]
        self.cost3 = ["brick", "brick", "brick"]
        self.cost4 = ["paper", "stone", "stone", "stone", "stone"]
        self.r1 = [(3, "vp")]
        self.r2 = [(5, "vp")]
        self.r3 = [(5, "vp")]
        self.r4 = [(7, "vp")]