from flask import Flask, render_template, redirect, request, session, url_for, jsonify
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
    database= os.getenv('DB_NAME')

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
    except Exception:
        return f"falise to acess tables in MYSQL"

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
        try:
            cursor = MYSQL_CONNECTION.cursor(dictionary=True)
            cursor.execute('SELECT * FROM users WHERE email = %s AND senha = %s', (email, senha))
            conta = cursor.fetchone()
            print(conta)
        except Exception as error:
            return f"falise to login in MYSQL: {error}"

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
@app.route("/adicionar_carrinho", methods=["POST"])
def adicionar_carrinho():
    if "id" not in session:
        return jsonify({"erro": "Usuário não autenticado"}), 401

    usuario_id = session["id"]
    hospedagem_id = request.json.get("hospedagem_id")
    quantidade = request.json.get("quantidade", 1)

    cursor = MYSQL_CONNECTION.cursor(dictionary=True)

    # Obtendo o preço da hospedagem
    cursor.execute("SELECT preco_diaria FROM hoteis WHERE id = %s", (hospedagem_id,))
    resultado = cursor.fetchone()
    
    
    if not resultado:
        return jsonify({"erro": "Hospedagem não encontrada"}), 404

    preco_diaria = resultado['preco_diaria']
    preco_total = preco_diaria * quantidade

    # Inserir no carrinho
    cursor.execute(
        "INSERT INTO carrinho (usuario_id, hospedagem_id, quantidade, preco_total) VALUES (%s, %s, %s, %s)",
        (usuario_id, hospedagem_id, quantidade, preco_total)
    )

    
    MYSQL_CONNECTION.commit()
    cursor.close()
    return jsonify({"mensagem": "Item adicionado ao carrinho!"})
'''
@app.route("/carrinho", methods=["GET"])
def ver_carrinho():
    if "id" not in session:
        return jsonify({"erro": "Usuário não autenticado"}), 401

    usuario_id = session["id"]
    try:
        cursor = MYSQL_CONNECTION.cursor(dictionary=True)
        cursor.execute("""
            SELECT c.id, h.nome, h.localizacao, c.quantidade, c.preco_total 
            FROM carrinho c 
            JOIN hoteis h ON c.hospedagem_id = h.id
            WHERE c.usuario_id = %s
        """, (usuario_id,))
        
        itens = cursor.fetchall()
        cursor.close()
    except mysql as error:
        return f"falise to load carrinho in MYSQL: {error}"

    return jsonify(itens)
'''


@app.route("/remover_carrinho/<int:item_id>", methods=["DELETE"])
def remover_carrinho(item_id):
    if "usuario_id" not in session:
        return jsonify({"erro": "Usuário não autenticado"}), 401
    try:
        cursor = MYSQL_CONNECTION.cursor(dictionary=True)
        cursor.execute("DELETE FROM carrinho WHERE id = %s", (item_id,))
        MYSQL_CONNECTION.commit()
        cursor.close()
    except mysql as error:
        return f"falise to delete tables in MYSQL: {error}"

    return jsonify({"mensagem": "Item removido do carrinho!"})



@app.route('/ver_carrinho', methods=['GET', 'POST'])
def carrinho():
    if 'id' not in session:
        return redirect(url_for('login'))
    id = session['id']
    
    cursor = MYSQL_CONNECTION.cursor(dictionary=True)
    query = """
        SELECT 
        carrinho.id, carrinho.preco_total, 
        hoteis.nome, hoteis.localizacao, hoteis.preco_diaria, hoteis.hotel_img_home
        FROM carrinho
        JOIN hoteis ON carrinho.hospedagem_id = hoteis.id
        WHERE carrinho.usuario_id = %s
         """
    cursor.execute(query, (id,))
    hoteis_no_carrinho = cursor.fetchall()
    cursor.close()
    print(hoteis_no_carrinho)


    return render_template('pageCarrinho.html', hotelCarrinho=hoteis_no_carrinho)


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