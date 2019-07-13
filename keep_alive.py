from flask import Flask, render_template
from threading import Thread


app = Flask('')

@app.route('/')
@app.route('/home')
def home():
    return "TODO:\n Add some kind of interface to show info like online users"

def run():
    app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
