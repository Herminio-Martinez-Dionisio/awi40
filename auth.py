import pyrebase
import firebase_config as token

firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth()

email="martinez@gmail.com"
password="123456"

user = auth.sign_in_with_email_and_password(email, password)
print(user['localId'])

email="herminio@gmail.com"
password="123456"
auth.create_user_with_email_and_password(email, password)