import requests
import json
import pandas

# get API key: https://developer.pubg.com/
api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIwYWM5NTU4MC1kY2EwLTAxMzctYWJlYi0wZjEwZDJiNjFmOTQiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTcyMzcwMzY1LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6Inl1d2VpLXpodTkzLWdtIn0.W4pWEkDZtsvZqz3QJ3QrNZQ_arBgTNnJYlDcRe77Qfg'

url = 'https://api.pubg.com/shards/'
platform = 'steam/'

headers = {'Authorization': 'Bearer ' + api_key,
           'Accept': 'application/vnd.api+json'}

'''
# get match samples
sample_url = url + platform + 'samples'
sample_response = requests.get(sample_url, headers=headers)
sample_data = json.loads(sample_response.text)
with open('sample_match.json', 'w') as fout:
    json.dump(sample_data,fout)


with open('sample_match.json') as fin:
    match_data = json.load(fin)

# get match list
match_list = [match['id'] for match in match_data['data']['relationships']['matches']['data']]
with open('sample_match_list.txt', 'w') as fout:
    for i in match_list:
        fout.write(i + '\n')

'''
# get match info for each match in the match list
match_list = []
with open('sample_match_list.txt') as fin:
    for line in fin:
        match_list.append(line.strip())

for match in match_list:
    match_url = url + platform + 'matches/' + match
    match_response = requests.get(match_url, headers = headers)
    #match_data = json.load(match_response.text)
    with open('matches_data.txt', 'a+') as fout:
        fout.write(match_response.text)

'''
# get leaderboard data
# not working now
game_mode = ['solo', 'duo', 'squad']

for game in game_mode:
    for i in range(2):
        lb_url = url + platform + 'leaderboards/' + game + '?page[number]=' + str(i)
        lb_response = requests.get(lb_url, headers=headers)
        if lb_response.status_code == 200:
            print('successfully scrapped. ' + game + ' page = ' + str(i))
            lb_data = json.loads(lb_response.text)
            print(lb_data['data']['relationships']['players'])
            with open('leaderboards_data.txt', 'a+') as fout:
                json.dump(lb_data, fout)
        else:
            print('fail'+ game + ' page = ' + str(i))
            '''









