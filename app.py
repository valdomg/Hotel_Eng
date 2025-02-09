from flask import Flask, render_template, redirect, request, session, url_for
import mysql.connector
from bdkeys import host, user, password, database

'''Configurações do Mysql'''

app = Flask(__name__)

app.config ['MYSQL_HOST'] = host()
app.config ['MYSQL_USER'] = user()
app.config ['MYSQL_PASSWORD'] = password()
app.config ['MYSQL_DB'] = database()

mysqlConnection = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB']
    )

'''
Arquivos de rotas para as páginas
'''
@app.route("/")
def home():
    try:
        cursor = mysqlConnection.cursor(dictionary=True)
        cursor.execute("SELECT *FROM hoteis")
        hotel = cursor.fetchall()
        cursor.close()

        print(hotel)
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

'''
Rota de carrinho
'''

'''
Rota de administrador
'''

if __name__ == '__main__':
    app.run(debug=True)