import web
import pyrebase
import firebase_config as token
import json

firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth()

urls = (
    '/registrar', 'Login',
    '/login', 'Login',
    '/correo_existe', 'Correo'
)
app = web.application(urls, globals())
render = web.template.render('views')

class Login:
    def GET(self):
        return render.registrar()

    def POST(self):
        try:
            formulario = web.input()
            email = formulario.email
            password = formulario.password
            print(email,password)
            print("Registrado")
            auth.create_user_with_email_and_password(email, password)
            return render.login()
        except Exception as error:
            formato = json.loads(error.args[1]) # Error en formato JSON
            error = formato['error'] # Se obtiene el json de error
            message = error['message'] # se obtiene el mensaje de error
            print("Error Login.POST: {}".format(message))
            #if message == "EMAIL_NOT_FOUND":
            return render.correo_existe()


if __name__ == "__main__":
    web.config.debug = False
    app.run()