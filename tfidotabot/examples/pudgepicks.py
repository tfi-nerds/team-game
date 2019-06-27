import tfidotabot
from tfidotabot.src import entities
import sys

#User inputs request for matches to query
matches_request = int(input("Enter amount of matches between 1 and 100 you wish to query : "))

print()

#Check if matches requested are betwen 1-100
if (matches_request > 100 or matches_request < 1):
    print('Invalid Entry. Try a number between 1 and 100.')
    sys.exit()

api = tfidotabot.APIWrapper('035E388F2B751358EB1098D99C365B86')

# Fetch amount of matches for Rahul requested by user
match_history = api.get_match_history(account_id=1234239, matches_requested= matches_request)

# Create dictionary to store counter
pudgepicks = {'npc_dota_hero_pudge': 0}

for match in match_history['matches']:
    for player in match['players']:
        hero_name = player['hero']['hero_name']
        steamid = player['steam_account']['id32']
        #Checks 2 conditions to determine if Rahul played pudge that match. Add's counter value to dictionary.
        if (hero_name == "npc_dota_hero_pudge" and steamid == 1234239):
            pudgepicks[hero_name] += 1

#Reads dictionary and assigns freq to the counter determined previously.
for hero_id, freq in pudgepicks.items():
    print ('Out of', matches_request, 'matches, Rahul picked Pudge', freq, 'times.')

