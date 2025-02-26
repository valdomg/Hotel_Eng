from flask import Flask, render_template, redirect, request, session, url_for
import mysql.connector
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, login_required, current_user

from dotenv import load_dotenv
import os


'''Configurações do Mysql'''

load_dotenv()


app = Flask(__name__)
MYSQL = MySQL(app)
lm = LoginManager(app)
app.secret_key = os.getenv('SECRET_KEY')

MYSQL_CONNECTION = mysql.connector.connect(
    host= os.getenv('DB_HOST'),
    user= os.getenv('DB_USER'),
    password= os.getenv('DB_PASSWORD'),
    database= os.getenv('DB_DATABASE')

)

#lm = LoginManager(app)


@lm.user_loader
def user_loader(id):
    cursor = MYSQL_CONNECTION.cursor()
    cursor.execute(f"SELECT *FROM users WHERE id={id}")
    usuario = cursor.fetchone()
    cursor.close()

    return usuario


'''
Arquivos de rotas para as páginas
'''
@app.route("/")
def home():
    #print(session['id'])
    try:
        cursor = MYSQL_CONNECTION.cursor(dictionary=True)
        cursor.execute("SELECT *FROM hoteis")
        hotel = cursor.fetchall()
        cursor.close()
    except mysql as error:
        return f"falise to acess tables in MYSQL: {error}"

    return render_template('index.html', hotel = hotel)

'''
Rota de login
'''
@app.route('/login', methods = ['GET', 'POST'])
def login():
    msg = ''
    
    if request.method == 'POST' and 'email' in request.form and 'senha' in request.form:
        print('AQUI')
        email = request.form['email']
        senha = request.form['senha']

        cursor = MYSQL_CONNECTION.cursor(dictionary=True)
        cursor.execute('SELECT * FROM users WHERE email = %s AND senha = %s', (email, senha))
        conta = cursor.fetchone()
        print(conta)

        ''''''
        if conta:
            session['loggedin'] = True
            session['id'] = conta ['id']
            session['username'] = conta ['nome']
            print('sucesso')
            return redirect(url_for("home"))
        else:
            msg = 'Dados Incorretos'

    return render_template('login.html', msg=msg)
'''Page usuario'''
@app.route('/usuario/<int:id>', methods=['GET'])
def usuario(id):

    if request.method == 'GET':
            cursor = MYSQL_CONNECTION.cursor(dictionary=True)
            cursor.execute(f'SELECT * FROM users WHERE id = {id}')
            usuario = cursor.fetchone()
            cursor.close()

    return render_template('pageUsuario.html', usuario=usuario)

'''Rota de carrinho'''

@app.route('/carrinho_de_compras/<int:id>', methods=['GET', 'POST'])
def carrinho(id):
    
    if request.method == 'GET':
            cursor = MYSQL_CONNECTION.cursor(dictionary=True)
            cursor.execute(f'SELECT * FROM hoteis WHERE id = {id}')
            hotelCarrinho = cursor.fetchone()
            cursor.close()

    #elif request.method == 'POST':


    return render_template('pageCarrinho.html', hotelCarrinho=hotelCarrinho)
'''rota de logout'''
@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', False)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('home'))
'''
Rota de cadastro
Paulo Braga
'''

'''
Rota de recuperação de senha
Yara
'''

'''
Rota de hotel
'''
@app.route('/hotel/<int:id>', methods = ['GET'])
def hotelPagina(id):

    try:
        if request.method == 'GET':
            cursor = MYSQL_CONNECTION.cursor(dictionary=True)
            cursor.execute(f'SELECT * FROM hoteis WHERE id = {id}')
            hotelCarac = cursor.fetchone()
            cursor.close()
            print(hotelCarac)
    except mysql as error:
        return f"falise to acess tables in MYSQL: {error}"
    
    return render_template('paginaHotel.html', hotelCarac=hotelCarac)
'''
Rota de carrinho
Valdemiro
'''

'''
Rota de administrador
'''

'''Rota de Quem Somos'''
@app.route('/QuemSomos')
def quemSomos():
     return render_template('quemSomos.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)