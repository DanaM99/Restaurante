from flask import Flask, request, jsonify, render_template
from controllers.auth_controller import auth_blueprint
from controllers.product_controller import product_blueprint
from controllers.cart_controller import cart_blueprint
from controllers.admin_controller import admin_blueprint
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Register blueprints
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(product_blueprint, url_prefix='/products')
app.register_blueprint(cart_blueprint, url_prefix='/cart')
app.register_blueprint(admin_blueprint, url_prefix='/admin')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
