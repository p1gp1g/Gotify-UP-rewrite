import requests
from base64 import b64decode

def send_to_gotify(b64endpoint,token,title,message,priority):
    try:
        data={
            'title': title,
            'message': message,
            'priority': priority
            }
        endpoint = b64decode(b64endpoint).decode()
        gotify_header = {'X-Gotify-Key': token}
        requests.post(
            endpoint + "/message",
            headers=gotify_header,
            json=data)
    except:
        pass
