from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

data = [
    {"id": 1, "name": "Nahdah", "status": "Active"},
    {"id": 2, "name": "Fauziah", "status": "Inactive"}
]

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


# HTTP handling request
@app.route('/data', methods=['GET'])
def getdata():
    return jsonify(data)

@app.route('/data', methods=['POST'])
def post_data():
    new_data = request.json
    if 'name' not in new_data or 'status' not in new_data:
        return jsonify({"error": "Missing 'name' or 'status' field"}), 400
    new_data['id'] = len(data) + 1 
    data.append(new_data)
    return jsonify(new_data), 201

@app.route('/data/<int:id>', methods=['PUT'])
def updateData(id):
    existing_data = next((item for item in data if item['id'] == id), None)
    if existing_data:
        updated_info = request.json
        existing_data.update(updated_info)
        return jsonify(existing_data)
    else:
        return jsonify({"message": "Data not found"}), 404

@app.route('/data/<int:id>', methods=['DELETE'])
def delete_data(id):
    global data
    item_to_delete = next((item for item in data if item['id'] == id), None)
    if item_to_delete is None:
        return jsonify({"error": f"Data with ID {id} not found"}), 404
    data = [item for item in data if item['id'] != id]
    return jsonify({"message": f"Data with ID {id} deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5467)
