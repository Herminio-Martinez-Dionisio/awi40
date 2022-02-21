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
    '/error_email','Error_email',
    '/logout','Logout',
    '/recuperar_password', 'recuperar'
)
app = web.application(urls, globals())
render = web.template.render('views')

class Logout:
    def GET(self):
        web.setcookie('localID', None)
        return render.login()

class Bienvenida:
    def GET(self):
        try:
            print("Bienvenida.GET localID: ",web.cookies().get('localID')) 
            if web.cookies().get('localID') == None:
                return render.login()
            else: 
                return render.bienvenida() 
        except Exception as error: 
            print("Error Bienvenida.GET: {}".format(error)) 

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
        #user = auth.sign_in_with_email_and_password(email, password)
        #print(user['localId'])
        #return render.login()              
        try:
            formulario = web.input()
            email = formulario.email
            password = formulario.password
            user = auth.sign_in_with_email_and_password(email, password)
            print(user['localId'])

            #informacion = auth.get_account_info(user['idToken'])
            #usuarios = informacion['users']
            #usuario = usuarios[0]
            #localid = usuario['localId']
            #web.setcookie('localid', localId)

            web.setcookie('localID', user['localId']) # se almacena en una cookie el localID
            print("localId : ",web.cookies().get('localID'))

            #message = "Bienvenido"
            #return render.login(message)
            return render.bienvenida()
        except Exception as error:
            formato = json.loads(error.args[1]) # Error en formato JSON
            error = formato['error'] # Se obtiene el json de error
            message = error['message'] # se obtiene el mensaje de error
            print("Error Login.POST: {}".format(message))
            if message == "EMAIL_NOT_FOUND":
                return render.error_email()
                #message1 = "Correo incorrecto"
            else:
                return render.error_cont()
                #message1 = "contraseña incorrecta"
            #return render.login(message1)
            #print(error['message'])
            #return render.login()
class recuperar_password:
    
    def GET(self):
        return web.seeother("recuperar_password")
    def POST(self):
        recuperar_datos = web.input()
        email = recuperar_datos.correo_r
        print(email, "recuperando contraseña")            

        result = auth.send_password_reset_email(email)
        print(result)    

if __name__ == "__main__":
    web.config.debug = False
    app.run()