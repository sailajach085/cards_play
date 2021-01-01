from cards import *
import pytest

def test_shuffleCards():
	cd = CardsGame()
	cd2 = CardsGame()
	cd.shuffleCards()
	assert cd.deck != cd2.deck,print("Shuffle Test Passed")

def test_getTopCard():
	cd = CardsGame()
	cd2 = CardsGame()
	tpl = cd.getTopCard()
	assert tpl[0]=="Spade" and tpl[1]==2,print("getTopCard Test Passed")

def test_sortCard():
    cd = CardsGame()
    tlist = [("Spade", 2), ("Diamond", 5), ("Spade", "king"), ("Heart", 3), ("Club", "ace") ]
    expList = [("Spade", 2), ("Spade", "king"), ("Diamond", 5), ("Heart", 3), ("Club", "ace")]
    rtList = cd.sortDeck(tlist)
    assert expList == rtList,print("card Sort Test Passed")