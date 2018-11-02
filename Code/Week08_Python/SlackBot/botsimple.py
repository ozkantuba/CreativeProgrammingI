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
 
# format the message
message = 'The ' + animal + ' ' + verb + ' through the ' + place + '.'
print message

# save your message for posterity
with open('Tweets.txt', 'a') as f:		# 'a' = append to the file, not overwrite everything :)
	f.write(message + '\n')				# be sure to add a line break so your tweets don't get mashed together

# Connect to Slack with our Oauth settings and post messages to general channel
print 'posting message...'

slack_client.api_call(
  "chat.postMessage",
  channel="#general",
  text=message
)