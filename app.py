from flask import Flask, render_template, redirect, request, session, url_for
import mysql.connector
from dotenv import load_dotenv
import os


'''Configurações do Mysql'''

load_dotenv()


app = Flask(__name__)

MYSQL_CONNECTION = mysql.connector.connect(
    host= os.getenv('DB_HOST'),
    user= os.getenv('DB_USER'),
    password= os.getenv('DB_PASSWORD'),
    database= os.getenv('DB_DATABASE')

)


'''
Arquivos de rotas para as páginas
'''
@app.route("/")
def home():
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

'''
Rota de cadastro
'''

'''
Rota de recuperação de senha
'''

'''
Rota de hotel
'''
@app.route('/hotel/<int:id>', methods = ['GET'])
def hotelPagina(id):

    try:
        if request.method == 'GET':
            cursor = MYSQL_CONNECTION.cursor()
            cursor.execute(f'SELECT * FROM hoteis WHERE id = {id}')
            hotel = cursor.fetchone()
            cursor.close()
    except mysql as error:
        return f"falise to acess tables in MYSQL: {error}"
    
    return render_template('paginaHotel.html', hotel = hotel)
'''
Rota de carrinho
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