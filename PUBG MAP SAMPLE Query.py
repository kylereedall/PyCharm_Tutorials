from jsonpath_rw import parse
import requests

matchurl = "https://api.playbattlegrounds.com/shards/pc-na/matches/"
sampleurl = "https://api.playbattlegrounds.com/shards/pc-na/samples"

header = {
  "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIwYjg1M2VhMC0zYmE4LTAxMzYtMDY5MC03ZGM0MmNhOWYyNjgiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTI2NTI0MTY3LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6Indob2tpbGxlZG1lLTZhNDM3OWJiLTBmZjAtNDFlYS1iZWE5LWIyMmRlYmFhNjdiYSIsInNjb3BlIjoiY29tbXVuaXR5IiwibGltaXQiOjEwfQ.xZhyOBrHB1qGYKOmzfi79kWSrMyry5tntb2VnJe-4cM",
  "Accept": "application/vnd.api+json"
}

minfo = requests.get(sampleurl, headers=header)
minfo2 = minfo.json()
#pprint.pprint(minfo2)

matchIDparse = parse('data.relationships.matches.data.[*].id')
for match in matchIDparse.find(minfo2):
    MatchINFO = requests.get(matchurl+match.value, headers=header)
    MatchINFO2 = MatchINFO.json()
    mode =  (MatchINFO2['data']['attributes']['gameMode'])
    map = (MatchINFO2['data']['attributes']['mapName'])
    print(mode + ' ' + map)
    f = open("Map.and.GameMode.txt","a+")
    f.write(mode + ' ' + map + '\n')
    f.close()
    #print(MatchINFO2['data']['attributes']['gameMode'])
    #print(MatchINFO2['data']['attributes']['mapName'])