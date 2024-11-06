from flask import Flask, render_template
app = Flask(__name__) # __name__ is a special variable in Python that is the name of the module.

@app.route('/') # This is a decorator that creates a mapping between the URL and the function.
@app.route('/home')
def home_page():
    homePage = render_template('home.html')
    return homePage

@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template('market.html', items=items)

