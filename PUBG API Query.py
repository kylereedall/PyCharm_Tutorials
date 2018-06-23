from jsonpath_rw import jsonpath, parse
import requests, pprint, json

#name = input("Please enter your PUBG playername: ")
name = "ItsKyle"
playerurl = "https://api.playbattlegrounds.com/shards/pc-na/players?filter[playerNames]="
matchurl = "https://api.playbattlegrounds.com/shards/pc-na/matches/"
sampleurl = "https://api.playbattlegrounds.com/shards/pc-na/samples"

header = {
  "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIwYjg1M2VhMC0zYmE4LTAxMzYtMDY5MC03ZGM0MmNhOWYyNjgiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTI2NTI0MTY3LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6Indob2tpbGxlZG1lLTZhNDM3OWJiLTBmZjAtNDFlYS1iZWE5LWIyMmRlYmFhNjdiYSIsInNjb3BlIjoiY29tbXVuaXR5IiwibGltaXQiOjEwfQ.xZhyOBrHB1qGYKOmzfi79kWSrMyry5tntb2VnJe-4cM",
  "Accept": "application/vnd.api+json"
}

PINFO = requests.get(playerurl+name, headers=header)
PINFO2 = PINFO.json()
pprint.pprint(PINFO2)
accountid = PINFO2['data'][0]['id']
print(name + " account id is " + accountid)

matchid = PINFO2['data'][0]['relationships']['matches']['data'][0]['id']
print("Most recent MatchID is: " + matchid)

testparse = parse('data.[0].relationships.matches.data.[*].id')
for match in testparse.find(PINFO2):
    #print("MatchID: " + match.value)
    MINFO = requests.get(matchurl+match.value, headers=header)
    MINFO2 = MINFO.json()
    #pprint.pprint(MINFO2)
    mapparse = parse ('data.attributes.mapName')
    for map in mapparse.find(MINFO2):
        print(map)