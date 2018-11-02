#LOOPING SLACK BOT
#Tuba Ozkan | 2018

import random  			# for selecting random elements from lists
import os               # for virtual environments
from slackclient import SlackClient
import time

# some lists for our bot
animals = [ 'fish', 'cat', 'zebra', 'sparrow', 'pterodactyl' ]
verbs =   [ 'waltzed', 'ran', 'crept', 'soared', 'swam' ]
places =  [ 'hotel', 'park', 'Louvre', 'sun' ]

# OAuth settings for Slack API 
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

# pick some random words for our message
animal = random.choice(animals)
verb =   random.choice(verbs)
place =  random.choice(places)

# we can also load words from a text file, which is very helpful
# for bots, where you might want a really big vocabulary and don't
# want to clog your source code
nouns = []												# create an empty list
with open('WordLists/SingularNouns.txt') as word_file:	# open the file's contents
	for line in word_file:								# iterate through all lines in the file
		word = line.strip()								# remove newline (\n) characters
		nouns.append(word)								# add to list of words!

message = None

#create a loop that runs/sends random messages to slack every 5 seconds
while True:

	# we pick a random word from our text file/noun list
	noun = random.choice(nouns)
	
	# format the message - only noun is random
	message = 'The ' + noun + ' ' + verb + ' through the ' + place + '.'
	print message

	# save your message for posterity
	with open('Messages.txt', 'a') as f:		# 'a' = append to the file, not overwrite everything :)
		f.write(message + '\n')				# be sure to add a line break so your tweets don't get mashed together

	print 'posting message...'

	# Connect to Slack with our Oauth settings and post messages to general channel
	slack_client.api_call(
		"chat.postMessage",
		channel="#general",
		text=message
	)
	# wait 5 seconds before running the next loop
	time.sleep(5)

