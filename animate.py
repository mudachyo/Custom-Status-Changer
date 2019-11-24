import requests
import json
import random
import threading

#your token goes here
token = ''

def change_status(char):
    p_headers = {"Authorization": token, "Content-Type": "application/json", "method": "PATCH"}
    s_params = {"custom_status": {"text": char, "emoji_id": None, "emoji_name": None, "expires_at": None}}
    p_params = json.dumps(s_params)
    req = requests.patch("https://discordapp.com/api/v6/users/@me/settings", headers=p_headers, data=p_params)
    print('Sent')


while True:
    if threading.active_count() <= 5:
        threading.Thread(target=change_status, args=(str(random.randint(0,99999)),)).start()