from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/contact', methods=['POST'])
def contact():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    print(f"Received: Name={name}, Email={email}, Message={message}")

    return jsonify({"message": "Your info has been received!"})

if __name__ == '__main__':
    app.run(debug=True)
