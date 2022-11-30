from flask import Flask, request, render_template
from db import connect


app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/quem_somos')
def quemsomos():
    return render_template('quem_somos.html')

@app.route('/usuario')
def user():
    connection = connect()

    cur = connection.cursor()
    command = f"""select * from usuarios"""
    cur.execute(command)
    usuarios = cur.fetchall()

    return render_template('usuario.html', usuarios=usuarios)

@app.route('/contato', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        email = request.form['femail']
        assunto = request.form['fassunto']
        descricao = request.form['fdescricao']
        connection = connect()

        cur = connection.cursor()
        command = f"""INSERT INTO usuarios(email, assunto, descricao) VALUES ('{email}', '{assunto}', '{descricao}')"""
        cur.execute(command)

        connection.commit()

        cur.close

        return "Contato Enviado!"
    return render_template('contato.html')




