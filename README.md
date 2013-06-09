----AVAILABLE METHODS FROM Player class----

purchase_resource(self, direc, res)
	''' direc = "l" or "r" (left or right neighbour)
	res = "wood", "ore", "brick", "stone", "glass", "cloth", "paper"
	
	will purchase res from neighbour in direc'''

check_resoures(self, c)
	'''check resources needed to play Card c.
	Returns list of lists each representing a different combination of resources that
	would satisfy cost of c. Satisfying any list will allow play. If return empty, already
	have necessary resources'''


----WHAT INFO DO I HAVE AVAILABLE TO ME?----

You have access to all attributes of the Player object passed through the
choose_card method.This includes all properties of the player.board Board object.
It does NOT include all properties of the player.left and player.right player objects
or other players accessed via the Table object passed through.
(i.e. you can look at what other players have played but not at their hands)



----COMPLETE THIS METHOD FOR CLASS YourNameAI----

def choose_card(self, player, table, typ):
	'''choose a card from hand of Player player to use
	typ = "normal" -> play card, must pay cost
	typ = "free" -> play card, free
	typ = "copy" -> copy card, free

	return tuple (card, action)

	action = "play" -> play card onto board
	action = "discard" -> play card into discard pile
	action = "wonder" -> play card to build wonder
	'''
