from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/home', methods=['GET'])
def home():
    return "Math API is running!"

@app.route('/add', methods=['GET'])
def add():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        result = a + b
    
        return jsonify({"operation": "addition", "a": a, "b": b, "result": result})
    except:
        return jsonify({"error": "Invalid input"}), 400

@app.route('/multiply', methods=['GET'])
def multiply():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        result = a * b
        return jsonify({"operation": "multiplication", "a": a, "b": b, "result": result})
    except:
        return jsonify({"error": "Invalid input"}), 400

@app.route('/divide', methods=['GET'])
def divide():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        if b == 0:
            return jsonify({"error": "Division by zero is not allowed"}), 400
        result = a / b
        return jsonify({"operation": "division", "a": a, "b": b, "result": result})
    except:
        return jsonify({"error": "Invalid input"}), 400

if __name__ == '__main__':
    app.run(debug=True)
