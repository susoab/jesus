import requests
 
api_token = '***'
base_url = 'https://api.chatwork.com/v2'
 
room_id = '66869579'
message = 'wassap wake up right now!!!'
 
post_message_url = '{}/rooms/{}/messages'.format(base_url, room_id)
headers = { 'X-ChatWorkToken': api_token }
params = { 'body': message }
 
response = requests.post(post_message_url, headers=headers, params=params)
print(response)