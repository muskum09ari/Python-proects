# Importing random module
import random

# Defining list of phrases which will help to build a story

Sentence_starter = ['About late 20th century ', ' In the around 100 years since', 'There was a time']
character = [' there lived a queen.',' there was a woman named Muskan Kumari',
			' there lived a shepherd.']
time = [' One day', ' One no-moon night']
story_plot = [' she was passing by',' she was going for hunting ']
place = [' the mountains', ' the garden']
second_character = [' She saw a woman', ' she saw a young and beautiful']
age = [' who seemed to be from boomer', ' who seemed very old and feeble']
work = [' rummaging something.', ' digging a well on roadside.']

# Selecting an item from each list and concatenating them.
print(random.choice(Sentence_starter)+random.choice(character)+
	random.choice(time)+random.choice(story_plot) +
	random.choice(place)+random.choice(second_character)+
	random.choice(age)+random.choice(work))
