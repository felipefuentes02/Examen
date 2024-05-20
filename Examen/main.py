from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])
        precio = 9000
        total = precio * cantidad

        if edad >= 18 and edad <= 30:
            descuento = int(total * 0.15)
        elif edad > 30:
            descuento = int(total * 0.25)
        else:
            descuento = 0

        totalDescuento = int(total - descuento)

        return render_template('ejercicio1.html', nombre=nombre, total=total, descuento=descuento, totalDescuento=totalDescuento)

    return render_template('ejercicio1.html')

usuarios = {
    'juan': 'admin',
    'pepe': 'user'
}

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = ''
    if request.method == 'POST':
        nombre = request.form['nombre']
        contrasena = request.form['contraseña']
        if nombre in usuarios and contrasena == usuarios[nombre]:
            if nombre == 'juan':
                mensaje = f'Bienvenido Administrador {nombre}'
            else:
                mensaje = f'Bienvenido Usuario {nombre}'
        else:
            mensaje = 'Usuario o contraseña incorrectos'
    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run()
