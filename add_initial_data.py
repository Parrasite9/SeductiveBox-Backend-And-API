from app import create_app, db
from app.models import Product, Style

app = create_app()

with app.app_context():
    # Add some styles
    style1 = Style(name='Lingerie Set')
    style2 = Style(name='Bodysuit')
    db.session.add_all([style1, style2])
    db.session.commit()

    # Add some products
    product1 = Product(name='Red Lace Set', item_number='001', price=49.99, style_id=style1.id)
    product2 = Product(name='Black Silk Bodysuit', item_number='002', price=59.99, style_id=style2.id)
    db.session.add_all([product1, product2])
    db.session.commit()

    print("Initial data added successfully.")
