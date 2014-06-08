# -*- coding: utf-8 -*-

"""
Word Ladder

Today we'll be designing a function that takes in two words and determines if it's possible to transform one word in to the other by changing one letter at a time (letters can not be added or removed, only changed). When a letter is changed the new word must also be a valid word. Each letter index can only be changed one time. Here is an example using "power" and "tuned":

power -> tower -> towed -> toned -> tuned
"""

"""
To install wordnet we need to do download the corpus
Fire up python console and run the following steps:
	import nltk
	nltk.download()
	
This would open up a downloader. Just search for "wordnet"
"""

from nltk import wordnet

def transform_words(word1, word2):
	"""
	The main method that checks to see if a word can be transformed word1 to
	word2
	"""
	pass
