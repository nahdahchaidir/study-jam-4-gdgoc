from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', title="Home Page")

@app.route('/about')
def about():
    return render_template('about.html', title="About Page")

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact Page")

@app.route('/data', methods=['GET'])
def getData():
    return jsonify({"message": "This is a GET request"})

@app.route('/data', methods=['POST'])
def postData():
    data = request.json
    return jsonify({"message": "This is a POST request", "data_received": data})

@app.route('/data/<int:id>', methods=['PUT'])
def putData(id):
    data = request.json
    return jsonify({"message": f"Data with ID {id} updated", "updated_data": data})

@app.route('/data/<int:id>', methods=['DELETE'])
def deleteData(id):
    return jsonify({"message": f"Data with ID {id} deleted"})

if __name__ == '__main__':
    app.run(debug=True, port=5467)
