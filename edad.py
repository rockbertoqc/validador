from flask import Flask, render_template, request

edad=Flask(__name__)

# Definimos la ruta y los métodos para pedir datos en formulario
@edad.route('/', methods=['GET', 'POST'])
def index():
    # La variable mensaje está vacía porque se llenará con el método POST que ingrese el usuario
    message=""

    if request.method == 'POST':
        # Age es un entero y se obtendrá de formulario (form); request.form se refiere a los datos enviados 
        # desde el formulario en la solicitud HTTP; estamos utilizando el método .get() en el diccionario request.form 
        # para obtener el valor del campo "age". La cadena "age" se pasa como argumento al método .get(), 
        # y si ese campo existe en el diccionario, el método devuelve su valor. Si el campo no existe, devuelve None.
        age = int(request.form.get('age'))
        # Hacemos la comparación
        if age >= 18:
            message = "Bienvenido"
        else:
            message = "No tienes permitido el ingreso"
            # Pasamos la variable message para que pueda ser utilizada dentro del template HTML 
            # y mostrar el mensaje correspondiente según la edad ingresada
    return render_template('index.html', message=message)

if __name__=="__main__":
    edad.run(debug=True)

