#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json
import pandas
from pathlib import Path

api_key = 'api_key'
# limit: 10 request per minute
api_key = Path(api_key).read_text().strip()
api_key


# In[48]:


url = 'https://api.pubg.com/shards/'
platform_list = ['steam/','console/','kakao/']

headers = {'Authorization': 'Bearer ' + api_key,
           'Accept': 'application/vnd.api+json'}


# In[49]:


# get match samples
match_list = []
for platform in platform_list:
    sample_url = url + platform + 'samples'
    sample_response = requests.get(sample_url, headers=headers)
    sample_data = json.loads(sample_response.text)
    for match in sample_data['data']['relationships']['matches']['data']:
        match_list.append(match['id'])


# In[50]:


len(match_list) # 2007 matches from three platforms


# In[ ]:


'type':'participant',
'id':'a0f0efc4-9298-4b57-8bbc-9aefbfea296c',
'attributes':{ 
   'stats':{ 
      'DBNOs':2,
      'assists':0,
      'boosts':6,
      'damageDealt':148.37,
      'deathType':'byplayer',
      'headshotKills':0,
      'heals':7,
      'killPlace':15,
      'killStreaks':1,
      'kills':2,
      'longestKill':8.659662,
      'name':'tianmijian',
      'playerId':'account.2f0ef27035fc43d8bc80b4b140d9718c',
      'revives':0,
      'rideDistance':0,
      'roadKills':0,
      'swimDistance':0,
      'teamKills':0,
      'timeSurvived':689.386,
      'vehicleDestroys':0,
      'walkDistance':497.25082,
      'weaponsAcquired':4,
      'winPlace':13
   },
   'actor':'',
   'shardId':'steam'
}
      },
      { 
'type':'roster',
'id':'17e53e6d-f28e-474a-b5b9-cfa1faa1f4bd',
'attributes':{ 
   'stats':{ 
      'rank':35,
      'teamId':6
   },
   'won':'false',
   'shardId':'steam'
},
'relationships':{ 
   'team':{ 
      'data':None
   },
   'participants':{ 
      'data':[ 
         { 
            'type':'participant',
            'id':'c4f285f7-d528-4e4f-9150-a4da285646dc'
         },
         { 
            'type':'participant',
            'id':'68ccad81-5411-4f9f-862e-9ff39ad45c3e'
         }
      ]
   }
}
      },


# In[66]:


all_rows = []


# In[67]:


for i,match in enumerate(match_list):
    match_url = url + platform + 'matches/' + match
    match_response = requests.get(match_url, headers = headers)
    # get match
    sample_match = json.loads(match_response.text)
    # get match attributes
    matchType = sample_match['data']['attributes']['gameMode']
    matchDuration = sample_match['data']['attributes']['duration']
    matchId = match
    # get player attributes
    included = sample_match['included']
    for obj in included:
        if obj['type'] == 'participant':
            player = obj['attributes']['stats']
            playerId = player['playerId']
            playerName = player['name']
            DBNOs = player['DBNOs']
            assists = player['assists']
            boosts = player['boosts']
            damageDealt = player['damageDealt']
            deathType = player['deathType']
            headshotKills = player['headshotKills']
            heals = player['heals']
            killPlace = player['killPlace']
            killStreaks = player['killStreaks']
            kills = player['kills']
            longestKill = player['longestKill']
            revives = player['revives']
            rideDistance = player['rideDistance']
            roadKills = player['roadKills']
            swimDistance = player['swimDistance']
            teamKills = player['teamKills']
            timeSurvived = player['timeSurvived']
            vehicleDestroys = player['vehicleDestroys']
            walkDistance = player['walkDistance']
            weaponsAcquired = player['weaponsAcquired']
            winPlace = player['winPlace']
            row = (playerId, matchId, assists, boosts,damageDealt,DBNOs,headshotKills,heals,killPlace,
                   kills,killStreaks,longestKill,matchDuration,matchType,revives,
                   rideDistance,roadKills,swimDistance,teamKills,vehicleDestroys,walkDistance,weaponsAcquired,winPlace)
            all_rows.append(row)


# In[68]:


len(all_rows) # 173087 rows


# In[77]:


columns = ["playerId", "matchId", "assists", "boosts","damageDealt","DBNOs","headshotKills","heals","killPlace","kills","killStreaks","longestKill","matchDuration","matchType","revives","rideDistance","roadKills","swimDistance","teamKills","vehicleDestroys","walkDistance","weaponsAcquired","winPlace"]


# In[78]:


import csv
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(columns)
    for row in all_rows:
        writer.writerow(row)


# In[ ]:




