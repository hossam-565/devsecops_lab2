from flask import Flask, request, jsonify

app = Flask(__name__)

#password = "MyHardcodedPass123"  # Intentional vulnerability for Bandit test


@app.route("/")
def home():
    return jsonify(message="Welcome to the Arithmetic API update 🔢")

@app.route("/add")
def add():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)
    return jsonify(operation="addition", a=a, b=b, result=a + b)

@app.route("/subtract")
def subtract():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)
    return jsonify(operation="subtraction", a=a, b=b, result=a - b)

@app.route("/multiply")
def multiply():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)
    return jsonify(operation="multiplication", a=a, b=b, result=a * b)

@app.route("/divide")
def divide():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)
    if b == 0:
        return jsonify(error="Division by zero is not allowed"), 400
    return jsonify(operation="division", a=a, b=b, result=a / b)

@app.route("/health")
def health():
    return jsonify(status="ok")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
