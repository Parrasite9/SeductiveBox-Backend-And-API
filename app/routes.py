from flask import request, jsonify, current_app as app
from . import db
from .models import User, Product, Variation, Style, Media

@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([product.name for product in products])

@app.route('/product/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    if product is None:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify({
        'name': product.name,
        'item_number': product.item_number,
        'price': product.price,
        'style_id': product.style_id
    })

@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(
        first_name=data['first_name'],
        last_name=data['last_name'],
        mailing_address=data['mailing_address'],
        billing_address=data['billing_address'],
        credit_card_number=data['credit_card_number'],
        credit_card_expiry=data['credit_card_expiry'],
        credit_card_cvv=data['credit_card_cvv']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201
