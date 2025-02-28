import firebase_admin
from firebase_admin import credentials, firestore, auth
from flask import Flask, request, jsonify

# Firebase credentials.json ko yaha set karo (Firebase Console se download karo)
cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
app = Flask(__name__)

# Route: Add User Data to Firestore
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    user_ref = db.collection('users').document(data['email'])
    user_ref.set(data)
    return jsonify({"message": "User Added Successfully!"})

# Route: Get All Users
@app.route('/get_users', methods=['GET'])
def get_users():
    users_ref = db.collection('users').stream()
    users = [{user.id: user.to_dict()} for user in users_ref]
    return jsonify(users)

# Route: Firebase Authentication (Signup User)
@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    user = auth.create_user(
        email=data['email'],
        password=data['password']
    )
    return jsonify({"message": "User Created!", "uid": user.uid})

if __name__ == '__main__':
    app.run(debug=True)
