import pyrebase
import firebase_config as token

firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth()
db = firebase.database()

nombre = input("Nombre: ")
telefono = input("Telefono: ")
email = input("Email: ")
password = input("contraseña: ")

user = auth.create_user_with_email_and_password(email, password)
print("localId: ",user['localId'])

data = {
    "nombre": nombre,
    "telefono": telefono,
    "email": email
}

results = db.child("users").child(user['localId']).set(data)

print(results)
