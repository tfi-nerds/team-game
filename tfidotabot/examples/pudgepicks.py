import tfidotabot

matches_request = 0
while(matches_request <= 0 or matches_request > 100):
    
    #User inputs request for matches to query
    matches_request = int(input("Enter amount of matches between 1 and 100 you wish to query : "))
    if (matches_request > 100 or matches_request < 1):
        #Prints error if input isnt 1-100
        print()
        print('Invalid Entry. Try a number between 1 and 100.')




    


#Registered API number goes here (RegisteredAPINumber)
api = tfidotabot.APIWrapper('RegisteredAPINumber')

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

