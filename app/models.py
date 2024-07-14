from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    mailing_address = db.Column(db.String(200), nullable=False)
    billing_address = db.Column(db.String(200), nullable=False)
    credit_card_number = db.Column(db.String(20), nullable=False)
    credit_card_expiry = db.Column(db.String(5), nullable=False)
    credit_card_cvv = db.Column(db.String(3), nullable=False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    item_number = db.Column(db.String(50), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    style_id = db.Column(db.Integer, db.ForeignKey('style.id'), nullable=False)

class Variation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    size = db.Column(db.String(10), nullable=False)
    color = db.Column(db.String(50), nullable=False)
    stock = db.Column(db.Integer, nullable=False)

class Style(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Media(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    url = db.Column(db.String(200), nullable=False)
