class Config(object):
    # Title of the notification
    TITLE = "Mastodon"
    # Content of the notificaiton
    # empty to forward the POST body
    MESSAGE = "You have received a new notification"
    # priority of the notification
    PRIORITY = 7
    # This relay URL
    # this is used only to register
    URL = "https://relay.example.tld/"
