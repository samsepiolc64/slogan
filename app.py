from flask import Flask, render_template, request, redirect, url_for, Response, flash, session


app = Flask(__name__)

@app.route('/')
def start():
    txt = "slogan"
    return render_template('index.html', txt=txt)
