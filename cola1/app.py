from flask import Flask, render_template, request, redirect, url_for
from banco import Banco

app = Flask(__name__)
banco = Banco()

@app.route('/')
def index():
    cliente_actual = banco.obtener_ultimo_atendido()
    return render_template('index.html', cliente_actual=cliente_actual)


@app.route('/agregar', methods=['POST'])
def agregar():
    nombre = request.form.get('nombre')
    if nombre:
        banco.llega_cliente(nombre)
    return redirect(url_for('index'))

@app.route('/atender', methods=['POST'])
def atender():
    banco.atender_cliente()
    return redirect(url_for('index'))

@app.route('/lista')
def lista():
    clientes = banco.obtener_clientes_en_espera()
    return render_template('lista.html', clientes=clientes)
    
if __name__ == '__main__':
    app.run(debug=True)
