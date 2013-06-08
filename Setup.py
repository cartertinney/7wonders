from PlayerClass import *

def setup(n):
    '''set up game for n players'''
    decks = setup_cards(n)
    ageIII = decks[2]
    ageII = decks[1]
    ageI = decks[0]
    players = []   #array of players
    #make array of AIs and give each player one of them
    ais = [1, 2, 3, 4, 5, 6, 7]
    for i in range(0, n):
        ai = ais[i]
        players.append(Player(ai))
    #set up right and left of players
    i = 0
    while i < len(players):
        curr = players[i]
        prev = players[i - 1]
        prev.left = curr
        curr.right = prev
        i += 1
    table = setup_boards(players)
    choose_wonder(players)
    table.decks = decks
    #deal out the first age
    deal(ageI, table.players)
    return table
    
def setup_boards(players):
    table = Table()
    table.players = players
    #add individual boards to table, and link discard pile
    for player in players:
        table.boards.append(player.board)
        player.board.discard = table.discard
    right = -1
    left = 1
    #curr = 0
    for board in table.boards:
        #set up left and right
        board.left = table.boards[left]
        board.right = table.boards[right]
        #copy table.boards and remove left, right, and self
        others = copy.copy(table.boards)
        others.remove(board)
        others.remove(board.left)
        others.remove(board.right)
        #increment left and right
        right = right + 1
        left = left + 1
        if left > len(table.boards) - 1:
            left = 0
    return table
        
        
       
def setup_cards(n):
    ageI = []
    ageII = []
    ageIII= []
    #add cards for 3+
    ageI.append(LumberYard())
    ageI.append(StonePit())
    ageI.append(ClayPool())
    ageI.append(OreVein())
    ageI.append(ClayPit())
    ageI.append(TimberYard())
    ageI.append(Loom())
    ageI.append(Glassworks())
    ageI.append(Press())
    ageI.append(Baths())
    ageI.append(Altar())
    ageI.append(Theater())
    ageI.append(EastTradingPost())
    ageI.append(WestTradingPost())
    ageI.append(Marketplace())
    ageI.append(Apothecary())
    ageI.append(Workshop())
    ageI.append(Scriptorium())
    ageI.append(Stockade())
    ageI.append(Barracks())
    ageI.append(GuardTower())
    
    ageII.append(Sawmill())
    ageII.append(Quarry())
    ageII.append(Brickyard())
    ageII.append(Foundry())
    ageII.append(Loom())
    ageII.append(Glassworks())
    ageII.append(Press())
    ageII.append(Aqueduct())
    ageII.append(Temple())
    ageII.append(Statue())
    ageII.append(Courthouse())
    ageII.append(Forum())
    ageII.append(Caravansery())
    ageII.append(Vineyard())
    ageII.append(Dispensary())
    ageII.append(Laboratory())
    ageII.append(Library())
    ageII.append(School())
    ageII.append(ArcheryRange())
    ageII.append(Stables())
    ageII.append(Walls())
    
    ageIII.append(Pantheon())
    ageIII.append(Gardens())
    ageIII.append(TownHall())
    ageIII.append(Palace())
    ageIII.append(Senate())
    ageIII.append(Haven())
    ageIII.append(Lighthouse())
    ageIII.append(Arena())
    ageIII.append(Lodge())
    ageIII.append(Observatory())
    ageIII.append(University())
    ageIII.append(Academy())
    ageIII.append(Study())
    ageIII.append(SiegeWorkshop())
    ageIII.append(Fortifications())
    ageIII.append(Arsenal())
    
    if n >= 4:
        #add cards for 4+
        ageI.append(LumberYard())
        ageI.append(OreVein())
        ageI.append(Excavation())
        ageI.append(Pawnshop())
        ageI.append(Tavern())
        ageI.append(Scriptorium())
        ageI.append(GuardTower())
        
        ageII.append(Sawmill())
        ageII.append(Quarry())
        ageII.append(Brickyard())
        ageII.append(Foundry())
        ageII.append(Bazar())
        ageII.append(Dispensary())
        ageII.append(TrainingGround())
        
        ageIII.append(Gardens())
        ageIII.append(Haven())
        ageIII.append(ChamberOfCommerce())
        ageIII.append(University())
        ageIII.append(Circus())
        ageIII.append(Arsenal())
                      
    if n >= 5:
        #add cards for 5+
        ageI.append(StonePit())
        ageI.append(ClayPool())
        ageI.append(ForestCave())
        ageI.append(Altar())
        ageI.append(Tavern())
        ageI.append(Apothecary())
        ageI.append(Barracks())
        
        ageII.append(Loom())
        ageII.append(Glassworks())
        ageII.append(Press())
        ageII.append(Caravansery())
        ageII.append(Courthouse())
        ageII.append(Laboratory())
        ageII.append(Stables())
        
        ageIII.append(TownHall())
        ageIII.append(Study())
        ageIII.append(Senate())
        ageIII.append(SiegeWorkshop())
        ageIII.append(Arena())
        ageIII.append(Circus())
        
    if n >= 6:
        #add cards for 6+
        ageI.append(TreeFarm())
        ageI.append(Mine())
        ageI.append(Loom())
        ageI.append(Glassworks())
        ageI.append(Press())
        ageI.append(Theater())
        ageI.append(Marketplace())
       
        ageII.append(Temple())
        ageII.append(Forum())
        ageII.append(Caravansery())
        ageII.append(Vineyard())
        ageII.append(Library())
        ageII.append(ArcheryRange())
        ageII.append(TrainingGround())
        
        ageIII.append(Pantheon())
        ageIII.append(TownHall())
        ageIII.append(Lighthouse())
        ageIII.append(ChamberOfCommerce())
        ageIII.append(Circus())
        ageIII.append(Lodge())
        
    if n >= 7:
        #add cards for 7+
        ageI.append(Pawnshop())
        ageI.append(Baths())
        ageI.append(Tavern())
        ageI.append(EastTradingPost())
        ageI.append(WestTradingPost())
        ageI.append(Workshop())
        ageI.append(Stockade())
        
        ageII.append(Aqueduct())
        ageII.append(Statue())
        ageII.append(Forum())
        ageII.append(Bazar())
        ageII.append(School())
        ageII.append(TrainingGround())
        ageII.append(Walls())
        
        ageIII.append(Palace())
        ageIII.append(Observatory())
        ageIII.append(Acadamy())
        ageIII.append(Arena())
        ageIII.append(Arsenal())
        ageIII.append(Fortifications())
        
        
        
        
        
    
    add_guilds(ageIII, n)
    #shuffle all three decks
    random.shuffle(ageI)
    random.shuffle(ageII)
    random.shuffle(ageIII)
    
    decks = []
    decks.append(ageI)
    decks.append(ageII)
    decks.append(ageIII)
    return decks
        
def add_guilds(deck, n):
    guilds = []
    #add all the guilds to the array
    guilds.append(WorkersGuild())
    guilds.append(CraftsmansGuild())
    guilds.append(TradersGuild())
    guilds.append(PhilosophersGuild())
    guilds.append(SpiesGuild())
    guilds.append(StrategistsGuild())
    guilds.append(ShipownersGuild())
    guilds.append(ScientistsGuild())
    guilds.append(MagistratesGuild())
    guilds.append(BuildersGuild())
    
    #randomize n+2 guilds to put in Age III
    random.shuffle(guilds)
    for i in range(0, n+2):
        g = guilds.pop()
        deck.append(g)
        
def choose_wonder(players):
    a = [RhodosA(), AlexandriaA(), EphesosA(), BabylonA(), OlympiaA(),\
         HalikarnassosA(), GizahA()]
    b = [RhodosB(), AlexandriaB(), EphesosB(), BabylonB(), OlympiaB(),\
         HalikarnassosB(), GizahB()]
    wonderidx = 6
    for player in players:
        i = random.randint(0, wonderidx)
        AB = ["A", "B"]
        side = AB[random.randint(0, 1)]
        if side == "A":
            wonder = a.pop(i)
            player.board.wonder = wonder
            b.pop(i)
            wonderidx -= 1
        elif side == "B":
            wonder = b.pop(i)
            player.board.wonder = wonder
            a.pop(i)
            wonderidx -= 1
        player.board.res[player.board.wonder.resource] += 1
    

def deal(deck, players):
    '''deal Deck deck to all players in array players'''
    #while there still exist cards in deck, deal
    while deck:
        for player in players:
            card = deck.pop()
            player.handbuf.append(card)