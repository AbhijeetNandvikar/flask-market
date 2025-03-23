import bcrypt
from flask_login import login_user
from market import app,db
from flask import render_template,redirect,url_for,flash
from market.models import Item,User
from market.forms import LoginForm, RegisterUserForm
from flask_login import login_user,logout_user,login_required

@app.route('/') # This is a decorator that creates a mapping between the URL and the function.
@app.route('/home')

def home_page():
    homePage = render_template('home.html')
    return homePage

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

@app.route('/register',methods=['GET','POST'])
def register_page():
    form = RegisterUserForm()
    if form.validate_on_submit():
        # check if user exists
        user_to_create = User(username=form.username.data,email_address=form.email_address.data,password=form.password1.data)
        # add user to db
        db.session.add(user_to_create)
        # commit to db
        db.session.commit()
        # flash message
        flash(f'Account created successfully! You are now able to login',category='success')
        # redirect to login page
        return redirect(url_for('login_page'))
    
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    
    return render_template('register.html',form=form)

@app.route('/login',methods=['GET','POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        # check if user exists
        attempted_user = User.query.filter_by(username=form.username.data).first()
        # check if password is correct using bcrypt to compare the password_hash and the attempted_password
        if attempted_user and attempted_user.check_password_correction(form.password.data):
            # if the user exists and the password is correct, log the user in
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}',category='success')
            # redirect to the market page
            return redirect(url_for('market_page'))
        else:
            flash('Username and password are not match! Please try again',category='danger')

    return render_template('login.html',form=form)