import requests
 
api_token = 'Your API token'
base_url = 'https://api.chatwork.com/v2'
 
room_id = 'rid66869579'
message = 'wassap shun'
 
post_message_url = '{}/rooms/{}/messages'.format(base_url, room_id)
headers = { 'X-ChatWorkToken': api_token }
params = { 'body': message }
 
response = requests.post(post_message_url, headers=headers, params=params)
print(response)