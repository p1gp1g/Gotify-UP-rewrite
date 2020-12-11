#!/usr/bin/env python3
from base64 import b64encode
from mastodon import Mastodon
from config import Config
from urllib.parse import quote_plus

instance_url = input("Mastodon instance: ")
username = input("Mastodon username: ")
password = input("Mastodon password: ")
got_endpoint = input("Gotify endpoint: ")
got_token = input("Gotify token: ")

Mastodon.create_app("mastodon-gotify",
    api_base_url=instance_url, 
    to_file="/tmp/app_token")

masto = Mastodon(
    client_id = "/tmp/app_token",
    api_base_url = instance_url
)

masto.log_in(
    username=username,
    password=password
)

endpoint = Config().URL + "/relay/" + quote_plus(b64encode(got_endpoint.encode())) + "/" + got_token
priv, pub = masto.push_subscription_generate_keys()
print(masto.push_subscription_set(
    endpoint=endpoint,
    encrypt_params=pub,
    follow_events = True,
    favourite_events = True,
    reblog_events = True,
    mention_events = True,
    poll_events = True,
    follow_request_events = True
))
