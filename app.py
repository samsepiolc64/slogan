from flask import Flask, render_template, request, redirect, url_for, Response, flash, session
from os import getenv
import openai
import os

openai.api_key  = getenv('API_KEY')
app = Flask(__name__)

@app.route('/')
def start():
    lamp_review = """
    Odkryj multifunkcyjną maskę do twarzy Skin Ready z serii INGLOT PLAYINN i pozwól swojej skórze poczuć TĘ MOC! Moc głębokiego nawilżenia, ujędrnienia oraz uczucia wygładzonej, aksamitnej skóry. Wypróbuj produkt, który wyrównuje drobne zmarszczki oraz opóźnia proces starzenia się skóry, wspomagając odnowę komórkową naskórka i wzmacniając jego strukturę.
    """
    prompt = f"""
    Napisz 5 haseł reklamowych dla tego produktu. \
    Niech hasło będzie maksymalnie z 10 wyrazów.
    Review text: '''{lamp_review}'''
    """
    response = get_completion(prompt)
    return render_template('index.html', txt=response)