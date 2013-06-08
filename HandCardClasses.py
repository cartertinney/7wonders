#class Hand:
    #def __init__(self):
        #self.arr = []
    
    #def add(self, c):
        #'''Add Card c to the Hand'''
        #self.arr.append(c)
    
    #def remove(self, c):
        #'''Remove Card c from the Hand'''
        #self.arr.remove(c)

class Card:
    def __init__(self):
        self.name = None    #name of card
        self.colour = None    #colour of card
        self.rescost = []    #resource cost of card
        self.mcost = 0    #monetary cost of card
        self.chain = None    #precursor in chain
        self.chain2 = None
        self.freebuild = None    #available freebuild
        self.freebuild2 = None    #available freebuild
        self.vp = 0    #victory points awarded
        self.money = 0    #money awarded
        self.stren = 0    #military strength provided
        self.symbol = None    #science type
        self.ability = None    #ability granted (e.g. trading post)
        self.res = []    #resource(s) granted
        self.update = None    #update vps. (dir, type, param, val)
                              #dir: lr, lrs, s (left, right, self)

#Infrastructure
class Pawnshop(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Pawnshop"
        self.colour = "blue"
        self.vp = 3

class Baths(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Baths"
        self.colour = "blue"
        self.rescost = ["stone"]
        self.freebuild = "Aqueduct"
        self.vp = 3
    
class Altar(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Altar"
        self.colour = "blue"
        self.freebuild = "Temple"
        self.vp = 2

class Theater(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Theater"
        self.colour = "blue"
        self.freebuild = "Statue"
        self.vp = 2
    
class Aqueduct(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Aqueduct"
        self.colour = "blue"
        self.rescost = ["stone", "stone", "stone"]
        self.chain = "Baths"
        self.vp = 5
        
class Temple(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Temple"
        self.colour = "blue"
        self.rescost = ["wood", "brick", "glass"]
        self.chain = "Altar"
        self.freebuild = "Pantheon"
        self.vp = 3
    
class Statue(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Statue"
        self.colour = "blue"
        self.rescost = ["wood", "ore", "ore"]
        self.chain = "Theater"
        self.freebuild = "Gardens"
        self.vp = 4

class Pantheon(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Pantheon"
        self.colour = "blue"
        self.rescost = ["brick", "brick", "ore", "paper", "cloth", "glass"]
        self.chain = "Temple"
        self.vp = 7

class Gardens(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Gardens"
        self.colour = "blue"
        self.rescost = ["wood", "brick", "brick"]
        self.chain = "Statue"
        self.vp = 5
    
class TownHall(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Town Hall"
        self.colour = "blue"
        self.rescost = ["glass", "ore", "stone", "stone"]
        self.vp = 6
    
class Palace(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Palace"
        self.colour = "blue"
        self.rescost = ["glass", "paper", "cloth", "brick", "wood", "ore", "stone"]
        self.vp = 8

class Courthouse(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Courthouse"
        self.colour = "blue"
        self.rescost = ["brick", "brick", "cloth"]
        self.chain = "Scriptorium"
        self.vp = 4
    
class Senate(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Senate"
        self.colour = "blue"
        self.rescost = ["ore", "stone", "wood", "wood"]
        self.chain = "Library"
        self.vp = 6
    
#Military
class Stockade(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Stockade"
        self.colour = "red"
        self.rescost = ["wood"]
        self.stren = 1
    
class Barracks(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Barracks"
        self.colour = "red"
        self.rescost = ["ore"]
        self.stren = 1
    
class GuardTower(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Guard Tower"
        self.colour = "red"
        self.rescost = ["brick"]
        self.stren = 1
    
class Walls(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Walls"
        self.colour = "red"
        self.rescost = ["stone", "stone", "stone"]
        self.freebuild = "Fortifications"
        self.stren = 2
    
class TrainingGround(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Training Ground"
        self.colour = "red"
        self.rescost = ["wood", "ore", "ore"]
        self.freebuild = "Circus"
        self.stren = 2

class Stables(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Stables"
        self.colour = "red"
        self.rescost = ["ore", "brick", "wood"]
        self.chain = "Apothecary"
        self.stren = 2
    
class ArcheryRange(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Archery Range"
        self.colour = "red"
        self.rescost = ["wood", "wood", "ore"]
        self.chain = "Workshop"
        self.stren = 2
    
class Fortifications(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Fortifications"
        self.colour = "red"
        self.rescost = ["stone", "ore", "ore", "ore"]
        self.chain = "Walls"
        self.stren = 3
    
class Circus(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Circus"
        self.colour = "red"
        self.rescost = ["stone", "stone", "stone", "ore"]
        self.chain = "Training Ground"
        self.stren = 3
    
class Arsenal(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Arsenal"
        self.colour = "red"
        self.rescost = ["ore", "wood", "wood", "cloth"]
        self.stren = 3
    
class SiegeWorkshop(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Siege Workshop"
        self.colour = "red"
        self.rescost = ["wood", "brick", "brick", "brick"]
        self.chain = "Laboratory"
        self.stren = 3
    
#Economy
class Tavern(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Tavern"
        self.colour = "yellow"
        self.money = 5

class EastTradingPost(Card):
    def __init__(self):
        Card.__init__(self)    
        self.name = "East Trading Post"
        self.colour = "yellow"
        self.freebuild = "Forum"
        self.ability = "rtrade"

class WestTradingPost(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "West Trading Post"
        self.colour = "yellow"
        self.freebuild = "Forum"
        self.ability = "ltrade"

class Marketplace(Card):
    def __init__(self):
        Card.__init__(self)   
        self.name = "Marketplace"
        self.colour = "yellow"
        self.ability = "reftrade"

class Forum(Card):
    def __init__(self):
        Card.__init__(self)    
        self.name = "Forum"
        self.colour = "yellow"
        self.rescost = ["brick", "brick"]
        self.chain = "East Trading Post"
        self.chain2 = "West Trading Post"
        self.freebuild = "Haven"
        self.res = ["wildref"]
        

class Caravansery(Card):
    def __init__(self):
        Card.__init__(self) 
        self.name = "Caravansery"
        self.colour = "yellow"
        self.rescost = ["wood", "wood"]
        self.chain = "Marketplace"
        self.freebuild = "Lighthouse"
        self.res = ["wildraw"]
        

class Vineyard(Card):
    def __init__(self):
        Card.__init__(self)   
        self.name = "Vineyard"
        self.colour = "yellow"
        self.update = [("lrs", "money", "brown", 1)]

class Bazar(Card):
    def __init__(self):
        Card.__init__(self)    
        self.name = "Bazar"
        self.colour = "yellow"
        self.update = [("lrs", "money", "grey", 2)]

class Haven(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Haven"
        self.colour = "yellow"
        self.rescost = ["cloth", "ore", "wood"]
        self.chain = "Forum"
        self.update = [("s", "vp/money", "brown", 1)]

class Lighthouse(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Lighthouse"
        self.colour = "yellow"
        self.rescost = ["glass", "ore"]
        self.chain = "Caravansery"
        self.update = [("s", "vp/money", "yellow", 1)]

class ChamberOfCommerce(Card):
    def __init__(self):
        Card.__init__(self)  
        self.name = "Chamber of Commerce"
        self.colour = "yellow"
        self.rescost = ["brick", "brick", "paper"]
        self.update = [("s", "vp", "grey", 2), ("s", "money", "grey", 2)]

class Arena(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Arena"
        self.colour = "yellow"
        self.rescost = ["ore", "stone", "stone"]
        self.chain = "Dispensary"
        self.update = [("s", "vp", "wonder", 1), ("s", "money", "wonder", 3)]

#Science
class Apothecary(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Apothecary"
        self.colour = "green"
        self.rescost = ["cloth"]
        self.freebuild = "Stables"
        self.freebuild2 = "Dispensary"
        self.symbol = "compass"
    
class Workshop(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Workshop"
        self.colour = "green"
        self.rescost = ["glass"]
        self.freebuild = "Archery Range"
        self.freebuild2 = "Laboratory"
        self.symbol = "gear"
    
class Scriptorium(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Scriptorium"
        self.colour = "green"
        self.rescost = ["paper"]
        self.freebuild = "Courthouse"
        self.freebuild2 = "Library"
        self.symbol = "tablet"

class Dispensary(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Dispensary"
        self.colour = "green"
        self.rescost = ["ore", "ore", "glass"]
        self.chain = "Apothecary"
        self.freebuild = "Arena"
        self.freebuild2 = "Lodge"
        self.symbol = "compass"
    
class Laboratory(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Laboratory"
        self.colour = "green"
        self.rescost = ["brick", "brick", "paper"]
        self.chain = "Workshop"
        self.freebuild = "Siege Workshop"
        self.freebuild2 = "Observatory"
        self.symbol = "gear"
    
class Library(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Library"
        self.colour = "green"
        self.rescost = ["stone", "stone", "cloth"]
        self.chain = "Scriptorium"
        self.freebuild = "Senate"
        self.freebuild2 = "University"
        self.symbol = "tablet"
    
class School(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "School"
        self.colour = "green"
        self.rescost = ["wood", "paper"]
        self.freebuild = "Academy"
        self.freebuild2 = "Study"
        self.symbol = "tablet"
    
class Lodge(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Lodge"
        self.colour = "green"
        self.rescost = ["brick", "brick", "cloth", "paper"]
        self.chain = "Dispensary"
        self.symbol = "compass"
    
class Observatory(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Observatory"
        self.colour = "green"
        self.rescost = ["ore", "ore", "glass", "cloth"]
        self.chain = "Laboratory"
        self.symbol = "gear"
    
class University(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "University"
        self.colour = "green"
        self.rescost = ["wood", "wood", "paper", "glass"]
        self.chain = "Library"
        self.symbol = "tablet"
    
class Academy(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Academy"
        self.colour = "green"
        self.rescost = ["stone", "stone", "stone", "glass"]
        self.chain = "School"
        self.symbol = "compass"
    
class Study(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Study"
        self.colour = "green"
        self.rescost = ["wood", "paper", "cloth"]
        self.chain = "School"
        self.symbol = "gear"
    
#Raw Resources

class LumberYard(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Lumber Yard"
        self.colour = "brown"
        self.res = ["wood"]

class StonePit(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Stone Pit"
        self.colour = "brown"
        self.res = ["stone"]
    
class ClayPool(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Clay Pool"
        self.colour = "brown"
        self.res = ["brick"]

class OreVein(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Ore Vein"
        self.colour = "brown"
        self.res = ["ore"]
        
class Sawmill(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Sawmill"
        self.colour = "brown"
        self.mcost = 1
        self.res = ["wood", "wood"]

class Quarry(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Quarry"
        self.colour = "brown"
        self.mcost = 1
        self.res = ["stone", "stone"]
    
class Brickyard(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Brickyard"
        self.colour = "brown"
        self.mcost = 1
        self.res = ["brick", "brick"]
    
class Foundry(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Foundry"
        self.colour = "brown"
        self.mcost = 1
        self.res = ["ore", "ore"]
        
class TreeFarm(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Tree Farm"
        self.colour = "brown"
        self.mcost = 1
        self.res = ("wood", "brick")

class Excavation(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Excavation"
        self.colour = "brown"
        self.mcost = 1
        self.res = ("stone", "brick")

class ClayPit(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Clay Pit"
        self.colour = "brown"
        self.mcost = 1
        self.res = ("brick", "ore")
    
class TimberYard(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Timber Yard"
        self.colour = "brown"
        self.mcost = 1
        self.res = ("stone", "wood")
    
class ForestCave(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Forest Cave"
        self.colour = "brown"
        self.mcost = 1
        self.res = ("wood", "stone")
    
class Mine(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Mine"
        self.colour = "brown"
        self.mcost = 1
        self.res = ("ore", "stone")
    
#Refined Resources    
class Loom(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Loom"
        self.colour = "grey"
        self.res = ["cloth"]
    
class Glassworks(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Glassworks"
        self.colour = "grey"
        self.res = ["glass"]
    
class Press(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Press"
        self.colour = "grey"
        self.res = ["paper"]
    
#Guilds
class WorkersGuild(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Workers Guild"
        self.colour = "purple"
        self.rescost = ["ore", "ore", "brick", "stone", "wood"]
        self.update = [("lr", "vp", "brown", 1)]

class CraftsmansGuild(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Craftsmans Guild"
        self.colour = "purple"
        self.rescost = ["ore", "ore", "stone", "stone"]
        self.update = [("lr", "vp", "grey", 2)]

class TradersGuild(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Traders Guild"
        self.colour = "purple"
        self.rescost = ["cloth", "paper", "glass"]
        self.update = [("lr", "vp", "yellow", 1)]
        
class PhilosophersGuild(Card):
    def __init__(self):
        Card.__init__(self)    
        self.name = "Philosophers Guild"
        self.colour = "purple"
        self.rescost = ["brick", "brick", "brick", "cloth", "paper"]
        self.update = [("lr", "vp", "green", 1)]

class SpiesGuild(Card):
    def __init__(self):
        Card.__init__(self)   
        self.name = "Spies Guild"
        self.colour = "purple"
        self.rescost = ["brick", "brick", "brick", "glass"]
        self.update = [("lr", "vp", "red", 1)]
            
class StrategistsGuild(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Strategists Guild"
        self.colour = "purple"
        self.rescost = ["ore", "ore", "stone", "cloth"]
        self.update = [("lr", "vp", "loss", 1)]
            
class ShipownersGuild(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Shipowners Guild"
        self.colour = "purple"
        self.rescost = ["wood", "wood", "wood", "paper", "glass"]
        self.update = [("s", "vp", "brown/grey/purple", 1)]
            
class ScientistsGuild(Card):
    def __init__(self):
        Card.__init__(self)    
        self.name = "Scientists Guild"
        self.colour = "purple"
        self.rescost = ["wood", "wood", "ore", "ore", "paper"]
        self.symbol = "wild"

class MagistratesGuild(Card):
    def __init__(self):
        Card.__init__(self)    
        self.name = "Magistrates Guild"
        self.colour = "purple"
        self.rescost = ["wood", "wood", "wood", "stone", "cloth"]
        self.update = [("lr", "vp", "blue", 1)]

class BuildersGuild(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Builders Guild"
        self.colour = "purple"
        self.rescost = ["stone", "stone", "brick", "brick", "glass"]
        self.update = [("lrs", "vp", "wonder", 1)]