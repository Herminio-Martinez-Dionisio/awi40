import web
import pyrebase
import firebase_config as token

firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth()

urls = (
    '/registrar', 'Login'
)
app = web.application(urls, globals())
render = web.template.render('views')

class Login:
    def GET(self):
        return render.registrar()

    def POST(self):
        formulario = web.input()
        email = formulario.email
        password = formulario.password
        print(email,password)
        print("Registrado")
        auth.create_user_with_email_and_password(email, password)
        return render.registrar()


if __name__ == "__main__":
    app.run()