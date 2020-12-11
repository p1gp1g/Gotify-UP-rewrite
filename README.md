# Mastodon-Gotify Push Gateway

This is a Push Gateway as simple as possible, designed for Mastodon/Pleroma to Gotify. It will probably work as it is with other project or with minor changes.

## Installation

### Dependencies

Dependencies are in requirements.txt.

Mastodon.py and cryptography are only needed to register to push notification on an Mastodon/Pleroma instance (for register.py).

### Nginx

A configuration like the following should work.

```
server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name relay.example.tld;


    ssl_certificate /opt/certs/relay.example.tld/crt.pem;
    ssl_certificate_key /opt/certs/relay.example.tld/key.pem;

    
    more_set_headers "Strict-Transport-Security : max-age=63072000; includeSubDomains; preload";

    location / {
			proxy_pass http://127.0.0.1:5001/;
      proxy_buffering  off;
      client_max_body_size  5M;
    }

    access_log /var/log/nginx/relay.example.tld-access.log;
    error_log /var/log/nginx/relay.example.tld-error.log;
}
```

### Systemd service

Edit masto2gotify.service and replace User, WorkingDirectory and ExecStart to match your configuration, then copy to in `/etc/systemd/system/masto2gotify.service` .

Finally, start the service and check its status:

```
systemctl start masto2gotify
systemctl status masto2gotify
```

## Registration

Push notifications are encrypted with the (Elliptic Curve) public key provided during push notification registration. 

### For developpers

If you want to user Gotify as a push provider for your android application (the forwarded notifications are coming soon), you will have to register for push notification from the application and store the key to decrypt the coming notifications.

"MESSAGE" in config.py needs to be empty to forward the notification body.

### For users without application

If you just want to get notified when you have a new notification on Mastodon without a specifique application, you can use this gateway too.

You should set a "MESSAGE" in config.py to not receive the content of the encrypted notification as a message.

To register to push notificaitions on your instance, you can use `register.py`.
