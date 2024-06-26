from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    return jsonify({"message": "Hello, World!", "user": "Yascher"})

@app.route('/api/data', methods=['POST'])
def data():
    data = request.json
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
