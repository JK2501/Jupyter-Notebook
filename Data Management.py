import requests

src = "Data.txt"
path = "https://euw1.api.riotgames.com/lol/match/v4/matchlists/by-account/"
accountID = "9ObJesSTXToff_Rr6ZYzKyQ5bNB904Y72MGoH879A7oI8vs"
key = "RGAPI-335c062b-c5e3-44a4-a843-20ef9b2c602d"
endIND = 1000
begIND = 900
params = {'endIndex': endIND, 'beginIndex': begIND, 'api_key': key}

response = requests.get(path+accountID, params=params).json()
matches = response['matches']
 
with open(src, 'a') as a:
    a.write('\n')
    for match in matches:
        a.write(str(match['gameId'])+'\n')
        
print('did ' + str(begIND) + ' until ' + str(endIND))        
