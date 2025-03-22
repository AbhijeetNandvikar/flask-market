from market import app
from flask import render_template
from market.models import Item


@app.route('/') # This is a decorator that creates a mapping between the URL and the function.
@app.route('/home')

def home_page():
    homePage = render_template('home.html')
    return homePage

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)
