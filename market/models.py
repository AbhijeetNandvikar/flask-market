from market import db, bcrypt, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username  = db.Column(db.String(length=30),nullable=False,unique=True)
    password_hash = db.Column(db.String(length=60),nullable=False)
    email_address = db.Column(db.String(length=50),nullable=False,unique=True)
    budget = db.Column(db.Integer,nullable=False,default=1000)
    items = db.relationship("Item", backref="owned_user",lazy=True)

    @property
    def password(self):
        return self.password
    
    @property
    def prettier_budget(self):
        if len(str(self.budget)) >= 4:
            return f'{str(self.budget)[:-3]},{str(self.budget)[-3:]}$'
        else:
            return f"{self.budget}$"
    
    @password.setter
    def password(self,plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode("utf-8")

    def check_password_correction(self,attempted_password):
        return bcrypt.check_password_hash(self.password_hash,attempted_password)    
    

    def __repr__(self):
        return f'item:{self.username}'


class Item(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(length=100),nullable=False,unique=True)
    barcode = db.Column(db.Integer,nullable=False,unique=True)
    price = db.Column(db.Integer,nullable=True,unique=True)
    description = db.Column(db.String(length=1024),nullable=False,unique=True)
    owner = db.Column(db.Integer,db.ForeignKey("user.id"))

    def __repr__(self):
        return f'item:{self.name}'

