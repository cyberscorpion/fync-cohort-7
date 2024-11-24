from flask import Flask, jsonify, request, render_template
from markupsafe import escape
from models import Products
from database import session
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route("/")
def homepage():
    get_Product()
    return render_template('homepage.html')

@app.route("/hello/")
@app.route("/hello/<name>")
def greet(name = None):
    return render_template('greet.html', name=name)

# @app.route("/products/", methods=['GET', 'POST'])
# def products():
#     if request.method == 'POST':
#         return "This is post call"
#     else:
#         return "<h1> Products </h1>"
    
@app.get("/products/")
def product_get():
    products = get_Product()
    return render_template('products.html', products = products)

@app.get("/deleteproduct/<int:id>/")
def deleteProduct(id):
    product = session.query(Products).filter_by(id = id).first()
    session.delete(product)
    session.commit()
    return "<h2> Product deleted </h2>"

    
@app.get("/addproduct/")
def product_add():
    return render_template('addProduct.html')


@app.post("/addproduct/")
def product_post():
    name = request.form['name']
    price = int(request.form['price'])
    quantity = int(request.form['quantity'])
    add_Product(name, price, quantity)
    return "<h2> Product Added </h2>"

@app.route("/products/<int:id>")
def product(id):
    return "<h2> Product details page to work </h2>"

# @app.route("/users/", methods=['GET', 'POST'])
# def users():
#     if request.method == 'POST':
#         firstName = request.form['fname']
#         lastName = request.form['lname']
#         print(request.form)
#         # do whatever you want with the values
#         return f"<h1> Users page: {firstName} {lastName} </h1>"
#     else:
#         firstName = request.args.get('fname')
#         lastName = request.args.get('lname', default="")
#         print(request.args)
#         # do whatever you want with the values
#         return f"<h1> Users page: {firstName} {lastName} </h1>"
    
@app.get("/users/")
def users_get():
    firstName = request.args.get('fname')
    lastName = request.args.get('lname', default="")
    print(request.args)
    # do whatever you want with the values
    return f"<h1> Users page: {firstName} {lastName} </h1>"

@app.post("/users/")
def users_post():
    firstName = request.form['fname']
    lastName = request.form['lname']
    print(request.form)
    # do whatever you want with the values
    return f"<h1> Users page: {firstName} {lastName} </h1>"

@app.route("/users/<username>/")
def user(username):
    return f"<h1> User: #{escape(username)} </h1>"

@app.route("/about/<path:subpath>/")
def about(subpath):
    return f"<h1> Path: #{escape(subpath)} </h1>"

def add_Product(name, price, quantity):
    product = Products(name = name, price = price, quantity = quantity)
    session.add(product)
    session.commit()

def get_Product():
    return session.query(Products).all()

## Rest APIs

@app.route("/api/data")
def getData():
    data = {
        'data' : 'Rajat Jain'
    }
    return jsonify(data)

class ProductResource(Resource):

    def get(self):
        products = get_Product()
        data = []
        for product in products:
            data.append({
                'id' : product.id,
                'name': product.name,
                'quantity' : product.quantity,
                'price': product.price
            })
        return jsonify(data)
    
class UserResource(Resource):
    def get(self):
        return jsonify({
            'user_count' : 3
        })
    
api.add_resource(ProductResource, '/api/products')
api.add_resource(UserResource, '/api/users')