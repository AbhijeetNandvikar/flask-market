from market import db



class Item(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(length=100),nullable=False,unique=True)
    barcode = db.Column(db.Integer,nullable=False,unique=True)
    price = db.Column(db.Integer,nullable=True,unique=True)
    description = db.Column(db.String(length=1024),nullable=False,unique=True)

    # def __repr__(self):
    #     return f'item:{self.name}'

