from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS

ProductDB = [
    {
        'id': '0',
        'name': 'test1',
        'section': 'A'
    },
    {
        'id': '1',
        'name': 'test2',
        'section': 'B'
    }
]

app = Flask(__name__)
CORS(app)


@app.route("/hello", methods=['GET'])
def welcome():
    return "welcome to python web service"


@app.route("/product/getProducts", methods=['GET'])
def getProducts():
    return jsonify({"products ": ProductDB})


@app.route("/product/getProduct/<name>", methods=['GET'])
def getProduct(name):
    product = [prod for prod in ProductDB if (prod['name'] == name)]
    return jsonify({"product ": product})


@app.route("/product/updateProduct/<name>", methods=['PUT'])
def updateProduct(name):
    product = [prod for prod in ProductDB if (prod['name'] == name)]

    if ('name' in request.json):
        print("Product Avalable")
        product[0]['name'] = request.json['name']
    return jsonify({"product ": product[0]})


@app.route("/product/addProduct", methods=['POST'])
def addProduct():
    ProductDB.append(request.json)
    return jsonify({"products ": ProductDB})


@app.route("/product/removeProduct/<name>", methods=['DELETE'])
def removeStudent(name):
    product = [prod for prod in ProductDB if (prod['name'] == name)]
    if (len(product) > 0):
        ProductDB.remove(product[0])
    return jsonify({"products ": ProductDB})


if (__name__ == "__main__"):
    app.run(host='0.0.0.0')
