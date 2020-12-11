from threading import Thread
from flask import request
from app.forward import send_to_gotify
from app import app

@app.route("/relay/<endpoint>/<token>",methods=["POST"])
def relay(endpoint,token):
    thread = Thread(target=send_to_gotify, args=(
        endpoint,
        token,
        app.config["TITLE"],
        app.config["MESSAGE"] or request.get_data().decode(),
        app.config["PRIORITY"]
        ))
    thread.daemon = True
    thread.start()
    return "ok"
