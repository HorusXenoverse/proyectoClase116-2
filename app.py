# importar modulos de la biblioteca Flask.
from flask import Flask , render_template

# crear objetos de la clase Flask, dando __name__ como argumento.
app = Flask(__name__)

# escribir las rutas usando las funciones "decorator".
# ruta o 'URL' predefinida.
@app.route("/")
def home():

    name = "Me" # escribe tu nombre
    age = "" # escribe tu edad

    return render_template('index.html' , name = name , age = age)

# define la ruta a la página web de tu padre.
@app.route("/padre")
def father():

    name = "Father" 
    age = "" 

    return render_template('father.html' , name = name , age = age)


# define la ruta a la página web de tu madre.
@app.route("/madre")
def mother():

    name = "Mother" 
    age = "" 

    return render_template('mother.html' , name = name , age = age)


# define la ruta a la página web de tus amigos.
@app.route("/amigo")
def friend():

    name = "friend" 
    age = "" 

    return render_template('friend.html' , name = name , age = age)


# agrega otras rutas, si tú quieres.




# ejecuta el archivo
if __name__  ==  '__main__':
    app.run(debug=True)
