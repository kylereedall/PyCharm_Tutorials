
#Calls recent data for ItsKyle
curl -X GET "https://api.playbattlegrounds.com/shards/pc-na/players?filter[playerNames]=ItsKyle" -H "accept: application/vnd.api+json" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIwYjg1M2VhMC0zYmE4LTAxMzYtMDY5MC03ZGM0MmNhOWYyNjgiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTI2NTI0MTY3LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6Indob2tpbGxlZG1lLTZhNDM3OWJiLTBmZjAtNDFlYS1iZWE5LWIyMmRlYmFhNjdiYSIsInNjb3BlIjoiY29tbXVuaXR5IiwibGltaXQiOjEwfQ.xZhyOBrHB1qGYKOmzfi79kWSrMyry5tntb2VnJe-4cM"

#Gets a match based on the matchID responses in the previous query
curl -X GET "https://api.playbattlegrounds.com/shards/pc-na/matches/d17bbd39-a86a-43db-a746-cbe098504aed" -H "accept: application/vnd.api+json" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIwYjg1M2VhMC0zYmE4LTAxMzYtMDY5MC03ZGM0MmNhOWYyNjgiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTI2NTI0MTY3LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6Indob2tpbGxlZG1lLTZhNDM3OWJiLTBmZjAtNDFlYS1iZWE5LWIyMmRlYmFhNjdiYSIsInNjb3BlIjoiY29tbXVuaXR5IiwibGltaXQiOjEwfQ.xZhyOBrHB1qGYKOmzfi79kWSrMyry5tntb2VnJe-4cM"


Dicts are contained within a pair of curly braces. {}
Lists are contained within brackets []
https://sdbrett.com/BrettsITBlog/2017/01/python-parsing-values-from-api-response/