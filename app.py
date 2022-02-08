import web
import pyrebase
import firebase_config as token
import json



firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth()


urls = (
    '/login', 'Login',
    '/bienvenida', 'Bienvenida',
    '/error_cont','Error_cont',
    '/error_email','Error_email'
)
app = web.application(urls, globals())
render = web.template.render('views')

class Login:
    def GET(self):
        return render.login()
        try:
            return render.login()
        except Exception as error:
            print("Error Login.GET: {}".format(error.args[0]))
    def POST(self):  
        formulario = web.input()
        email = formulario.email
        password = formulario.password
        user = auth.sign_in_with_email_and_password(email, password)
        print(user['localId'])
        return render.login()              
        try:
            message = None
            formulario = web.input()
            email = formulario.email
            password = formulario.password
            user = auth.sign_in_with_email_and_password(email, password)
            print(user['localId'])
            message = "Bienvenido"
            #return render.login(message)
            return web.seeother("bienvenida")
            #return render.bienvenida()
        except Exception as error:
            formato = json.loads(error.args[1]) # Error en formato JSON
            error = formato['error'] # Se obtiene el json de error
            message = error['message'] # se obtiene el mensaje de error
            print("Error Login.POST: {}".format(message))
            if message == "EMAIL_NOT_FOUND":
                #return render.error_email()
                message1 = "Correo incorrecto"
            else:
                #return render.error_cont()
                message1 = "contraseña incorrecta"
            return render.login(message1)
            print(error['message'])
            #return render.login()
            
            

if __name__ == "__main__":
    web.config.debug = False
    app.run()