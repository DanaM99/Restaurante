from flask import Blueprint, request, jsonify, render_template
from server.models import db, Product

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin', methods=['GET'])
def admin_page():
    return render_template('admin.html')

@admin_bp.route('/admin/products', methods=['POST'])
def add_product():
    data = request.json
    new_product = Product(name=data['name'], price=data['price'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product added successfully'})

@admin_bp.route('/admin/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{'name': p.name, 'price': p.price} for p in products])

@admin_bp.route('/admin/products/<int:id>', methods=['PUT', 'DELETE'])
def modify_product(id):
    product = Product.query.get(id)
    if request.method == 'PUT':
        data = request.json
        product.name
