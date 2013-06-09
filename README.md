----available methods from Player class---

purchase_resource(self, direc, res)
  ''' direc = "l" or "r" (left or right neighbour)
	res = "wood", "ore", "brick", "stone", "glass", "cloth", "paper"
	
	will purchase res from neighbour in direc'''

check_resoures(self, c)
	'''check resources needed to play Card c.
	Returns list of lists each representing a different combination of resources that
	would satisfy cost of c. Satisfying any list will allow play. If return empty, already
	have necessary resources'''





----COMPLETE THIS METHOD FOR CLASS YourNameAI----

def choose_card(self, player, typ):
	'''choose a card from hand of Player player to use
	typ = "normal" -> play card, must pay cost
	typ = "free" -> play card, free
	typ = "copy" -> copy card, free

	return tuple (card, action)

	action = "play" -> play card onto board
	action = "discard" -> play card into discard pile
	action = "wonder" -> play card to build wonder
	'''
