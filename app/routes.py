from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/oferta')
def offer():
    return render_template('offer.html')

@app.route('/firma')
def about():
    return render_template('about.html')

@app.route('/kontakt')
def contact():
    return render_template('contact.html')
