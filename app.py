from flask import Flask, render_template, redirect, request, session, url_for, jsonify
import mysql.connector
from flask_mysqldb import MySQL

from dotenv import load_dotenv
import os


'''Configurações do Mysql'''

load_dotenv()


app = Flask(__name__)
MYSQL = MySQL(app)

app.secret_key = os.getenv('SECRET_KEY')

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
    #print(session['id'])
    try:
        cursor = MYSQL_CONNECTION.cursor(dictionary=True)
        cursor.execute("SELECT *FROM hoteis")
        hotel = cursor.fetchall()
       
        cursor.execute("SELECT *FROM residencia")
        residencias = cursor.fetchall()
        cursor.close()
        
    except Exception:
        return f"falise to acess tables in MYSQL"

    return render_template('index.html', hotel = hotel, residencias = residencias)

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

'''Rota de pesquisa'''
@app.route('/pesquisa', methods=['GET'])
def pesquisa():
    
    termo = request.args.get('termo').lower()
    
    if termo == 'residencia' or termo == 'residência' or termo == 'residências':
        query = 'SELECT id, nome, localizacao, preco_diaria, residencia_img_home AS img_home FROM residencia'
    if termo == 'hotel' or termo == 'hoteis' or termo == 'hotéis':
        query = 'SELECT id, nome, localizacao, preco_diaria, hotel_img_home AS img_home FROM hoteis'
   
    cursor = MYSQL_CONNECTION.cursor(dictionary=True)
    cursor.execute(query)
    pesquisa = cursor.fetchall()
    print(pesquisa)
    cursor.close()

    return render_template('pagePesquisa.html', pesquisa=pesquisa, termo=termo )

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
        return redirect(url_for('home'))

    usuario_id = session["id"]
    hospedagem_id = request.json.get("hospedagem_id")
    quantidade = request.json.get("quantidade", 1)
    tipo_hospedagem = request.json.get("tipo_hospedagem")

    print(tipo_hospedagem)

    cursor = MYSQL_CONNECTION.cursor(dictionary=True)

    # Obtendo o preço da hospedagem
    if tipo_hospedagem == 'hotel':  
        cursor.execute("SELECT preco_diaria FROM hoteis WHERE id = %s", (hospedagem_id,))
    elif tipo_hospedagem == 'residencia':
        cursor.execute("SELECT preco_diaria FROM residencia WHERE id = %s", (hospedagem_id,))
    else:
        resultado = None
    

    resultado = cursor.fetchone()
    
    
    if not resultado:
        return jsonify({"erro": "Hospedagem não encontrada"}), 404

    preco_diaria = resultado['preco_diaria']
    preco_total = preco_diaria * quantidade

    # Inserir no carrinho
    cursor.execute(
        "INSERT INTO carrinho (usuario_id, hospedagem_id, tipo_hospedagem ,quantidade, preco_total) VALUES (%s, %s, %s, %s, %s)",
        (usuario_id, hospedagem_id, tipo_hospedagem ,quantidade, preco_total)
    )

    
    MYSQL_CONNECTION.commit()
    cursor.close()
    return jsonify({"mensagem": "Item adicionado ao carrinho!"})


@app.route("/remover_carrinho/<int:item_id>", methods=["DELETE"])
def remover_carrinho(item_id):
    if "id" not in session:
        return jsonify({"erro": "Usuário não autenticado"}), 401
    try:
        cursor = MYSQL_CONNECTION.cursor(dictionary=True)
        cursor.execute("DELETE FROM carrinho WHERE id = %s ", (item_id,))
        MYSQL_CONNECTION.commit()
        cursor.close()
        return jsonify({"success": True, "message": "Item removido com sucesso!"})

    
    except mysql as error:
        return f"falise to delete tables in MYSQL: {error}"

    return redirect(url_for('carrinho'))



@app.route('/ver_carrinho', methods=['GET', 'POST'])
def carrinho():
    if 'id' not in session:
        return redirect(url_for('login'))
    id = session['id']
    
    cursor = MYSQL_CONNECTION.cursor(dictionary=True)
    query = """
       SELECT c.id AS carrinho_id, c.usuario_id, c.quantidade, c.preco_total, 
       h.nome AS hospedagem_nome, h.localizacao, h.preco_diaria, 
       h.hotel_img_home AS img_home, h.categoria, h.descricao , 'hotel' AS tipo
        FROM carrinho c
        JOIN hoteis h ON c.hospedagem_id = h.id

        UNION

        SELECT c.id AS carrinho_id, c.usuario_id, c.quantidade, c.preco_total, 
            r.nome AS hospedagem_nome, r.localizacao, r.preco_diaria, 
            r.residencia_img_home AS img_home, r.categoria, r.descricao,'residencia' AS tipo
        FROM carrinho c
        JOIN residencia r ON c.hospedagem_id = r.id

        WHERE c.usuario_id = %s;


         """
    cursor.execute(query, (id,))
    
    hoteis_no_carrinho = cursor.fetchall()
    print(hoteis_no_carrinho)
    cursor.close()
    


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
@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "GET":
        return render_template("cadastroUsuario.html")

    elif request.method == "POST":
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        cursor = MYSQL_CONNECTION.cursor(dictionary=True)

        # Verifica se o e-mail já está cadastrado
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        usuario_existente = cursor.fetchone()

        if usuario_existente:
            cursor.close()
            return "Erro: Este e-mail já está cadastrado!"

        # Inserindo novo usuário
        query = "INSERT INTO users (nome, email, senha) VALUES (%s, %s, %s)"
        cursor.execute(query, (nome, email, senha))

        MYSQL_CONNECTION.commit()
        cursor.close()

        return redirect(url_for('login'))



'''
Rota de recuperação de senha
Yara
'''
@app.route("/redefinir-senha", methods=["GET"])
def redefinir_senha():
    return render_template("redefinir_senha.html")

@app.route("/definir-senha", methods=["POST"])
def definir_senha():
    email = request.form['email']
    nova_senha = request.form['senha']
    
    # Criptografar a senha (se necessário)
    # nova_senha = bcrypt.generate_password_hash(nova_senha).decode('utf-8')
    
    cursor = MYSQL_CONNECTION.cursor()
    
    query = "UPDATE users SET senha = %s WHERE email = %s"
    cursor.execute(query, (nova_senha, email))
    
    MYSQL_CONNECTION.commit()
    cursor.close()
    
    return redirect(url_for('login'))
'''
Rota de admin
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
            
    except mysql as error:
        return f"falise to acess tables in MYSQL: {error}"
    
    return render_template('paginaHotel.html', hotelCarac=hotelCarac)

@app.route('/residencia/<int:id>', methods = ['GET'])
def residenciaPagina(id):
    try:
        if request.method == 'GET':
            cursor = MYSQL_CONNECTION.cursor(dictionary=True)
            cursor.execute(f'SELECT * FROM residencia WHERE id = {id}')
            residenciaCarac = cursor.fetchone()
            cursor.close()
            
    except mysql as error:
        return f"falise to acess tables in MYSQL: {error}"
    
    return render_template('paginaResidencia.html', residenciaCarac=residenciaCarac)

'''
Rota de administrador
'''

'''Rota de Quem Somos'''
@app.route('/QuemSomos')
def quemSomos():
     return render_template('quemSomos.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)